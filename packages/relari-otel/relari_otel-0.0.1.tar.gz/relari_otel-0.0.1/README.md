# Relari-OTel

The `relari-otel package provides a lightweight wrapper around OpenTelemetry primitives for tracing LLM applications and send the traces to a collector.
This repository is met to be used with [Agent-Contracts](https://github.com/relari-ai/agent-contracts)

## Quickstart

First, install the package, specifying the instrumentations you want to use.

For example, to install the package with OpenAI and Langchain/Langgraph instrumentations:

```bash
pip install 'relari-otel[langchain,openai]'
```

Initialize the telemetry in your code

```python
Relari.init(project_name="Your Project Name")
```

### Certification

If you intend to use the certification feature (see [agent-contracts docs](https://agent-contracts.relari.ai/certification/certification)) you need to add the `vertification` extra:

```python
pip install 'relari-otel[langchain,openai,certification]'
```

## Instrumentation

All your framework and models are instrumented automatically.
However OpenTelemetry does not know how your code is structured.
To wrap all the spans in a trace you can use

```python
with Relari.start_new_sample(scenario_id="scenario_A"):
    await my_agent_code(specs["scenario_A"]["data"])
```

or alternative to run an evaluation over a specification

```python
async def runnable(data: Any):
    agent_inputs = prepare_my_agent_input(data)
    return my_agent_code(agent_inputs)

await Relari.eval_runner(specs=specs, runnable=runnable)
```

## Acknowledgements

Autoinstrumentations are provided by [Arize](https://github.com/Arize-ai/openinference)
