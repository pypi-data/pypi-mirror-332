from abc import ABC, abstractmethod
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, field_serializer

from relari_otel.utils import nanoid


# https://www.ietf.org/rfc/rfc2119.txt
class Level(Enum):
    MUST = "must"
    SHOULD = "should"


class RequirementRegistry:
    _registry: dict[str, type] = {}

    @classmethod
    def register(cls, subclass: type) -> None:
        cname = subclass.__name__
        if cname in {"BasePrecondition", "BasePathcondition", "BasePostcondition"}:
            # Do not register the base classes
            return
        if cname in cls._registry:
            raise RuntimeError(f"Requirement {cname} already registered")
        cls._registry[cname] = subclass

    @classmethod
    def get(cls, req_type: str) -> type:
        if req_type not in cls._registry:
            raise ValueError(f"Requirement {req_type} not registered")
        return cls._registry[req_type]


class _RequirementInterface(BaseModel, ABC):
    uuid: str = Field(
        default_factory=lambda: f"req-{nanoid(8)}",
        description="Unique identifier for the requirement",
    )
    name: str = Field(..., description="Name of the requirement")
    level: Level = Field(
        default=Level.MUST, description="Level of the requirement (MUST, SHOULD)"
    )

    def __init_subclass__(cls, **kwargs):
        RequirementRegistry.register(cls)
        super().__init_subclass__(**kwargs)

    def to_dict(self) -> dict:
        data = self.model_dump()
        data["type"] = self.__class__.__name__
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "_RequirementInterface":
        data = dict(data)
        data.pop("type", None)
        return cls.model_validate(data)

    @field_serializer("level")
    def serialize_level(self, level: Level):
        return level.value

    @property
    @abstractmethod
    def type(self) -> Literal["precondition", "pathcondition", "postcondition"]:
        raise NotImplementedError("Subclasses must implement type()")


class BasePrecondition(_RequirementInterface):
    @property
    def type(self) -> Literal["precondition"]:
        return "precondition"


class BasePathcondition(_RequirementInterface):
    @property
    def type(self) -> Literal["pathcondition"]:
        return "pathcondition"


class BasePostcondition(_RequirementInterface):
    on: Literal["output", "conversation"] = Field(
        ..., description="Type of input required for the requirement"
    )

    @property
    def type(self) -> Literal["postcondition"]:
        return "postcondition"


Requirement = BasePrecondition | BasePathcondition | BasePostcondition


## Instantiables


class Pathcondition(BasePathcondition):
    requirement: str = Field(...)

    def __init__(self, requirement: str, **kwargs):
        if "name" not in kwargs:
            kwargs["name"] = requirement
        super().__init__(requirement=requirement, **kwargs)

    @property
    def name(self) -> str:
        return self.requirement


class Postcondition(BasePostcondition):
    requirement: str = Field(...)

    def __init__(self, requirement: str, **kwargs):
        if "name" not in kwargs:
            kwargs["name"] = requirement
        super().__init__(requirement=requirement, **kwargs)

    @property
    def name(self) -> str:
        return self.requirement


class Precondition(BasePrecondition):
    requirement: str = Field(...)

    def __init__(self, requirement: str, **kwargs):
        if "name" not in kwargs:
            kwargs["name"] = requirement
        super().__init__(requirement=requirement, **kwargs)
