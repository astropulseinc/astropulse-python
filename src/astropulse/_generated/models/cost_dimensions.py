# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CostDimensions(BaseModel):
    """
    CostDimensions
    """ # noqa: E501
    cpu_core_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="cpuCoreHours")
    cpu_usage_core_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Consumed CPU core-hours. CPUCoreHours above is the allocated (requested) amount, which is what spend is billed against; this is what the workload actually used. Comparing the two is what separates an idle over-provisioned workload from a right-sized one. Absent when the source cannot report usage.", alias="cpuUsageCoreHours")
    cpu_utilization_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="CPU used as a percentage of CPU allocated, already divided over matching windows. Use this rather than dividing CPUUsageCoreHours by CPUCoreHours: usage is optional per window, so those two totals can cover different window counts and their ratio is wrong.", alias="cpuUtilizationPercent")
    efficiency_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The single headline for how much of what a workload reserved it actually used: CPU and memory usage over CPU and memory allocation, weighted by allocated hours. Storage and GPU are not included. It is a weighted mean of CPUUtilizationPercent and RAMUtilizationPercent below and therefore always lies between whichever of those are present, which is what lets it be rendered as their headline. When no window reported usage it falls back to the source's own efficiency figure. Absent when neither is available, and may exceed 100 when a workload consumes more than it reserved.", alias="efficiencyPercent")
    gpu_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gpuHours")
    network_gb: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The data the workloads sent, in gigabytes, leaving out pods on the host network. It is measured and not priced: no cost includes network traffic.", alias="networkGB")
    pv_gb_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pvGBHours")
    ram_gb_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ramGBHours")
    ram_usage_gb_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Consumed memory GB-hours, paired with RAMGBHours the same way CPUUsageCoreHours is paired with CPUCoreHours.", alias="ramUsageGBHours")
    ram_utilization_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The memory equivalent of CPUUtilizationPercent.", alias="ramUtilizationPercent")
    __properties: ClassVar[List[str]] = ["cpuCoreHours", "cpuUsageCoreHours", "cpuUtilizationPercent", "efficiencyPercent", "gpuHours", "networkGB", "pvGBHours", "ramGBHours", "ramUsageGBHours", "ramUtilizationPercent"]

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
        """Create an instance of CostDimensions from a JSON string"""
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
        """Create an instance of CostDimensions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpuCoreHours": obj.get("cpuCoreHours"),
            "cpuUsageCoreHours": obj.get("cpuUsageCoreHours"),
            "cpuUtilizationPercent": obj.get("cpuUtilizationPercent"),
            "efficiencyPercent": obj.get("efficiencyPercent"),
            "gpuHours": obj.get("gpuHours"),
            "networkGB": obj.get("networkGB"),
            "pvGBHours": obj.get("pvGBHours"),
            "ramGBHours": obj.get("ramGBHours"),
            "ramUsageGBHours": obj.get("ramUsageGBHours"),
            "ramUtilizationPercent": obj.get("ramUtilizationPercent")
        })
        return _obj


