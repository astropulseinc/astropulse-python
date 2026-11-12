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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.instance_type import InstanceType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class EKSAutoModeConfig(BaseModel):
    """
    EKSAutoModeConfig
    """ # noqa: E501
    enable_gpu_node_pool: Optional[StrictBool] = Field(default=None, description="Lets EKS Auto Mode provision GPU instances (optional, default false). AWS owns the NVIDIA driver and device plugin on these nodes; AstroPulse renders only the NodePool. Nodes are tainted nvidia.com/gpu:NoSchedule, so pods need a matching toleration.", alias="enableGpuNodePool")
    gpu_capacity_types: Optional[List[InstanceType]] = Field(default=None, description="The purchase options the GPU pool may buy: `OnDemand`, `Spot` or both. A new cluster's pool buys `OnDemand`, and an existing one keeps what it buys unless this is set.", alias="gpuCapacityTypes")
    gpu_limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(default=None, description="The maximum number of GPUs the GPU node pool may provision, counted across the pool (optional, 1-1000, default 10). Ignored unless the GPU node pool is enabled.", alias="gpuLimit")
    __properties: ClassVar[List[str]] = ["enableGpuNodePool", "gpuCapacityTypes", "gpuLimit"]

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
        """Create an instance of EKSAutoModeConfig from a JSON string"""
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
        """Create an instance of EKSAutoModeConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enableGpuNodePool": obj.get("enableGpuNodePool"),
            "gpuCapacityTypes": obj.get("gpuCapacityTypes"),
            "gpuLimit": obj.get("gpuLimit")
        })
        return _obj


