# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.gateway_scaling_metric import GatewayScalingMetric
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GatewayAutoScalingConfig(BaseModel):
    """
    GatewayAutoScalingConfig
    """ # noqa: E501
    enabled: Optional[StrictBool] = Field(default=None, description="Turns automatic scaling of the gateway proxy on.")
    max_replicas: Optional[StrictInt] = Field(default=10, description="The most copies that may run. Left out, it is 10.", alias="maxReplicas")
    metric: Optional[GatewayScalingMetric] = Field(default=None, description="What scaling follows. Left out, it is `CPU`.")
    min_replicas: Optional[StrictInt] = Field(default=2, description="The fewest copies that keep running. Left out, it is 2.", alias="minReplicas")
    target_cpu_percent: Optional[StrictInt] = Field(default=70, description="The average CPU use, in percent, that scaling keeps each copy at. Left out, it is 70.", alias="targetCPUPercent")
    target_requests_per_second: Optional[StrictInt] = Field(default=500, description="The requests per second each copy handles before another is added. Left out, it is 500.", alias="targetRequestsPerSecond")
    __properties: ClassVar[List[str]] = ["enabled", "maxReplicas", "metric", "minReplicas", "targetCPUPercent", "targetRequestsPerSecond"]

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
        """Create an instance of GatewayAutoScalingConfig from a JSON string"""
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
        """Create an instance of GatewayAutoScalingConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enabled": obj.get("enabled"),
            "maxReplicas": obj.get("maxReplicas") if obj.get("maxReplicas") is not None else 10,
            "metric": obj.get("metric"),
            "minReplicas": obj.get("minReplicas") if obj.get("minReplicas") is not None else 2,
            "targetCPUPercent": obj.get("targetCPUPercent") if obj.get("targetCPUPercent") is not None else 70,
            "targetRequestsPerSecond": obj.get("targetRequestsPerSecond") if obj.get("targetRequestsPerSecond") is not None else 500
        })
        return _obj


