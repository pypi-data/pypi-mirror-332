from opentelemetry.context import get_value, attach, get_current, set_value, Context
from opentelemetry import trace
from typing import Optional

ASSOCIATION_PROPERTIES = "relari.properties"

def _set_association_properties_attributes(span, properties: dict) -> None:
    for key, value in properties.items():
        span.set_attribute(f"{ASSOCIATION_PROPERTIES}.{key}", value)


def update_association_properties(
    properties: dict,
    set_on_current_span: bool = True,
    context: Optional[Context] = None,
) -> None:
    """Only adds or updates properties that are not already present"""
    association_properties = get_value("association_properties", context) or {}
    association_properties.update(properties)

    attach(set_value("association_properties", association_properties, context))

    if set_on_current_span:
        span = trace.get_current_span()
        _set_association_properties_attributes(span, properties)
