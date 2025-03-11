import asyncio
import hashlib
import json
import logging
import os
import time
from contextlib import contextmanager
from contextvars import Context
from typing import Any, Callable, Optional

from openinference.semconv.resource import ResourceAttributes
from openinference.semconv.trace import SpanAttributes
from opentelemetry import context as context_api
from opentelemetry import trace
from opentelemetry import trace as trace_api
from opentelemetry.context import attach, detach
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor

from relari_otel.semcov import (
    CertificationAttributes,
    EvalAttributes,
    EvalSpanAttributes,
)
from relari_otel.specifications import Specifications


from .tracing import update_association_properties
from .utils import json_dumps

logging.basicConfig(level=logging.INFO)

MAX_MANUAL_SPAN_PAYLOAD_SIZE = 1024 * 1024  # 1MB


class Relari:
    __tracer_name = "relari-otel"
    __initialized: bool = False
    __redis: Optional["Redis"] = None
    __certification_enabled: bool = False
    
    @classmethod
    def init(
        cls,
        api_key: str = os.getenv("RELARI_API_KEY", None),
        endpoint: str = "http://localhost:4318/v1/traces",
        project_name: str = "default",
        certification_enabled: bool = False,
        exclude_instrumentators: list[str] = [],
        batch: bool = True,
        redis_host: str = "localhost",
        redis_port: int = 6379,
    ):
        if not api_key:
            raise ValueError("RELARI_API_KEY is not set")
        if batch and certification_enabled:
            raise ValueError("Batch mode is not supported with certification enabled")
        run_id = hashlib.blake2b(os.urandom(64), digest_size=4).hexdigest()
        resource = Resource.create(
            {
                "service.name": cls.__tracer_name,
                ResourceAttributes.PROJECT_NAME: project_name,
                EvalAttributes.RUN_ID: run_id,
                CertificationAttributes.CERTIFICATION_ENABLED: certification_enabled,
            }
        )
        tracer_provider = TracerProvider(resource=resource)
        span_exporter = OTLPSpanExporter(
            endpoint=endpoint,
            headers={"X-API-Key": api_key},
        )
        span_processor = (
            BatchSpanProcessor(span_exporter=span_exporter)
            if batch
            else SimpleSpanProcessor(span_exporter=span_exporter)
        )
        tracer_provider.add_span_processor(span_processor)
        tracer_provider._default_processor = True
        trace_api.set_tracer_provider(tracer_provider)
        exclude_openai = False
        if "langchain" not in exclude_instrumentators:
            try:
                from langchain_core.messages import HumanMessage
            except ImportError:
                logging.info("LangChain not installed, skipping instrumentation")
                pass
            else:
                from openinference.instrumentation.langchain import (
                    LangChainInstrumentor,
                )

                exclude_openai = True
                logging.info("LangChain installed, instrumenting")
                LangChainInstrumentor().instrument(tracer_provider=tracer_provider)
        if "openai" not in exclude_instrumentators and not exclude_openai:
            from openinference.instrumentation.openai import OpenAIInstrumentor

            OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
        cls.__initialized = True
        try:
            from redis import Redis
            try:
                cls.__redis = Redis(host=redis_host, port=redis_port)
                cls.__certification_enabled = certification_enabled
            except Exception:
                if certification_enabled:
                    raise ValueError("Failed to connect to Redis")
                cls.__redis = None
                cls.__certification_enabled = False
        except ImportError:
            cls.__redis = None
            cls.__certification_enabled = False
        

    @classmethod
    def is_initialized(cls):
        """Check if Relari is initialized. A utility to make sure other
        methods are called after initialization.

        Returns:
            bool: True if Relari is initialized, False otherwise
        """
        return cls.__initialized

    @classmethod
    def is_certification_enabled(cls):
        """Check if certification is enabled.

        Returns:
            bool: True if certification is enabled, False otherwise
        """
        return cls.__certification_enabled

    @classmethod
    def get_trace_id(cls):
        """Get the trace id for the current trace.

        Returns:
            str: Trace id for the current trace
        """
        try:
            span_ctx = trace.get_current_span().get_span_context()
            return "{trace:032x}".format(trace=span_ctx.trace_id)
        except Exception:
            return None

    @classmethod
    @contextmanager
    def get_tracer(cls):
        try:
            yield trace.get_tracer(cls.__tracer_name)
        finally:
            pass

    @classmethod
    def set_metadata(cls, metadata: dict[str, str]):
        """Set the metadata for the current trace.

        Args:
            metadata (dict[str, str]): Metadata to set for the trace. Willl be\
                sent as attributes, so must be json serializable.
        """
        props = {f"metadata.{k}": json_dumps(v) for k, v in metadata.items()}
        update_association_properties(props)

    @classmethod
    @contextmanager
    def start_new_sample(
        cls,
        dataset_id: Optional[str] = None,
        scenario_id: Optional[str] = None,
        context: Optional[Context] = None,
    ):
        """Start a new span as the current setting the corresponding dataset/scenario id.

        Usage example:
        ```python
        with Relari.start_new_sample(scenario_id="my-sccenario-id") as sample:
            await my_async_function()
        ```

        Args:
            dataset_id (Optional[str], optional): id of the dataset
            scenario_id (Optional[str], optional): id of the scenario
            context (Optional[Context], optional): raw OpenTelemetry context\
                to attach the span to. Defaults to None.
        """

        if not cls.is_initialized():
            yield
            return

        with cls.get_tracer() as tracer:
            ctx = context or context_api.get_current()
            ctx_token = attach(ctx)
            attributes = {
                SpanAttributes.OPENINFERENCE_SPAN_KIND: EvalSpanAttributes.TYPE,
            }
            if dataset_id:
                attributes[EvalAttributes.DATASET_ID] = dataset_id
            if scenario_id:
                attributes[EvalAttributes.SCENARIO_ID] = scenario_id
            with tracer.start_as_current_span(
                EvalSpanAttributes.NAME,
                context=ctx,
                attributes=attributes,
            ) as span:
                yield span

            # TODO: Figure out if this is necessary
            try:
                detach(ctx_token)
            except Exception:
                pass

    @classmethod
    def set_input(cls, input: Any = None):
        """Set the input of the current span. Useful for manual
        instrumentation or to set preconditions.

        Args:
            input (Any, optional): input of the span. Will be sent as an\
                attribute, so must be json serializable. Defaults to None.
        """
        span = trace.get_current_span()
        if input is not None and span != trace.INVALID_SPAN:
            serialized_input = json_dumps(input)
            if len(serialized_input) > MAX_MANUAL_SPAN_PAYLOAD_SIZE:
                span.set_attribute(
                    EvalAttributes.OUTPUT,
                    "Error: output too large (relari-otel)",
                )
            else:
                span.set_attribute(EvalAttributes.INPUT, serialized_input)

    @classmethod
    def set_output(cls, output: Any = None):
        """Set the output of the current span. Useful for manual
        instrumentation or to set postconditions.

        Args:
            output (Any, optional): output of the span. Will be sent as an\
                attribute, so must be json serializable. Defaults to None.
        """
        span = trace.get_current_span()
        if output is not None and span != trace.INVALID_SPAN:
            serialized_output = json_dumps(output)
            if len(serialized_output) > MAX_MANUAL_SPAN_PAYLOAD_SIZE:
                span.set_attribute(
                    EvalAttributes.OUTPUT,
                    "Error: output too large (relari-otel)",
                )
            else:
                span.set_attribute(EvalAttributes.OUTPUT, serialized_output)

    @classmethod
    async def _runnable_wrapper(cls, dataset_id, scenario, runnable, **kwargs):
        with Relari.start_new_sample(
            dataset_id=dataset_id, scenario_id=scenario.uuid
        ) as sample:
            if asyncio.iscoroutinefunction(runnable):
                out = await runnable(scenario.data, **kwargs)
            else:
                out = runnable(scenario.data, **kwargs)
            Relari.set_output(out)

    @classmethod
    async def eval_runner(
        cls,
        specs: Specifications,
        runnable: Callable,
        batch_size: Optional[int] = None,
        **kwargs,
    ):
        batch_size = batch_size or len(specs)
        for i in range(0, len(specs.scenarios), batch_size):
            batch = specs.scenarios[i : i + batch_size]
            tasks = [
                asyncio.create_task(
                    cls._runnable_wrapper(specs.uuid, scenario, runnable, **kwargs)
                )
                for scenario in batch
            ]
            await asyncio.gather(*tasks)

    @classmethod
    def get_cert(cls, trace_id: Optional[str] = None):
        if not cls.is_certification_enabled():
            logging.info("Certification is not enabled, skipping get cert")
            return None
        if not trace_id:
            trace_id = cls.get_trace_id()
        result = cls.__redis.get(f"certificates:{trace_id}")
        if result:
            return json.loads(result)
        return None

    @classmethod
    def wait_for_cert(
        cls,
        polling_interval: int = 1,
        trace_id: Optional[str] = None,
        timeout: int = 60,
    ):
        start_time = time.time()
        while True:
            cert = cls.get_cert(trace_id)
            if cert:
                return cert
            if time.time() - start_time > timeout:
                raise TimeoutError("Timeout waiting for cert")
            time.sleep(polling_interval)
