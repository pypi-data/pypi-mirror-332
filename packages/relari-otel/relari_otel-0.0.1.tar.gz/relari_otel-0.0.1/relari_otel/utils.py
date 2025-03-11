import json
import logging
import random
from string import ascii_lowercase, digits
from typing import Any

import pydantic


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, pydantic.BaseModel):
            return o.model_dump_json()
        try:
            return super().default(o)
        except TypeError:
            return str(o)  # Fallback to string representation for unsupported types


def json_dumps(data: dict) -> str:
    try:
        return json.dumps(data, cls=CustomJSONEncoder)
    except Exception:
        # Log the exception and return a placeholder if serialization completely fails
        logging.warning("Failed to serialize data to JSON, type: %s", type(data))
        return "{}"  # Return an empty JSON object as a fallback


def nanoid(size: int = 8):
    return "".join(random.choices(ascii_lowercase + digits, k=size))
