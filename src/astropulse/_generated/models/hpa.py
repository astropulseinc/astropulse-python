# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class HPA(BaseModel):
    """
    HPA
    """ # noqa: E501
    cpu_utilization_percentage: Annotated[int, Field(le=100, strict=True, ge=20)] = Field(description="The target CPU utilization percentage for scaling (required, range: 20-100)", alias="cpuUtilizationPercentage")
    enabled: StrictBool = Field(description="Enables or disables the horizontal pod autoscaler (required)")
    max_replicas: Annotated[int, Field(strict=True, ge=1)] = Field(description="The maximum number of pod replicas (required, minimum: 1, must be >= MinReplicas)", alias="maxReplicas")
    memory_utilization_percentage: Annotated[int, Field(le=100, strict=True, ge=20)] = Field(description="The target memory utilization percentage for scaling (required, range: 20-100)", alias="memoryUtilizationPercentage")
    min_replicas: Annotated[int, Field(strict=True, ge=1)] = Field(description="The minimum number of pod replicas (required, minimum: 1)", alias="minReplicas")
    __properties: ClassVar[List[str]] = ["cpuUtilizationPercentage", "enabled", "maxReplicas", "memoryUtilizationPercentage", "minReplicas"]

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of HPA from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HPA from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpuUtilizationPercentage": obj.get("cpuUtilizationPercentage"),
            "enabled": obj.get("enabled"),
            "maxReplicas": obj.get("maxReplicas"),
            "memoryUtilizationPercentage": obj.get("memoryUtilizationPercentage"),
            "minReplicas": obj.get("minReplicas")
        })
        return _obj


