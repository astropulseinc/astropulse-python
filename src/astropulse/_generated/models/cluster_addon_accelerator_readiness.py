# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonAcceleratorReadiness(BaseModel):
    """
    ClusterAddonAcceleratorReadiness
    """ # noqa: E501
    declared_accelerators: Optional[StrictInt] = Field(default=None, description="How many NVIDIA devices the cluster's node groups can ever run. Zero on a cluster with no accelerator node group.", alias="declaredAccelerators")
    gpu_nodes: Optional[StrictStr] = Field(default=None, description="Says how many NVIDIA GPU nodes the cluster runs now and in which pools, or \"Nothing to check yet: no GPU nodes\". Empty when the cluster has not reported its nodes.", alias="gpuNodes")
    karpenter_gpu_pool: Optional[StrictBool] = Field(default=None, description="Reports a configured GPU node pool (the Karpenter add-on's or EKS Auto Mode's), which provisions accelerator nodes on demand: zero declared accelerators with this set is still a cluster that will produce measurements, once a GPU node exists.", alias="karpenterGpuPool")
    measurable: Optional[StrictBool] = Field(default=None, description="Whether anything on this cluster will report: an NVIDIA node group, or a GPU node pool.")
    vendors: Optional[List[StrictStr]] = Field(default=None, description="The accelerator vendors the cluster's node groups declare (nvidia, amd, google, xilinx), sorted. A vendor here that is not nvidia is why Warning is present.")
    warning: Optional[StrictStr] = Field(default=None, description="The one sentence to show when the install will work but measure nothing, or less than the cluster's accelerators suggest.")
    __properties: ClassVar[List[str]] = ["declaredAccelerators", "gpuNodes", "karpenterGpuPool", "measurable", "vendors", "warning"]

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
        """Create an instance of ClusterAddonAcceleratorReadiness from a JSON string"""
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
        """Create an instance of ClusterAddonAcceleratorReadiness from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "declaredAccelerators": obj.get("declaredAccelerators"),
            "gpuNodes": obj.get("gpuNodes"),
            "karpenterGpuPool": obj.get("karpenterGpuPool"),
            "measurable": obj.get("measurable"),
            "vendors": obj.get("vendors"),
            "warning": obj.get("warning")
        })
        return _obj


