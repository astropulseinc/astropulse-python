# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from astropulse._generated.models.accelerator_vendor import AcceleratorVendor
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AcceleratorMetricsSummary(BaseModel):
    """
    AcceleratorMetricsSummary
    """ # noqa: E501
    devices: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The range-wide figures, each weighted by window length and each resting only on the windows that carried it.")
    hardware_slowdown_fraction: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean fraction (0..1) of the range the hardware slowed a device, for a power brake or a fault.", alias="hardwareSlowdownFraction")
    measured_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How much of the requested range had stored windows behind it.", alias="measuredSeconds")
    memory_total_bytes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="memoryTotalBytes")
    memory_used_bytes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="memoryUsedBytes")
    power_cap_fraction: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean fraction (0..1) of the range a device was slowed to stay under its power limit.", alias="powerCapFraction")
    power_watts: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="powerWatts")
    sm_occupancy: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="smOccupancy")
    source: Optional[StrictStr] = Field(default=None, description="The exporter they were read from, as on AcceleratorMetrics.")
    temperature_celsius: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="temperatureCelsius")
    thermal_fraction: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean fraction (0..1) of the range a device was slowed because it ran too hot.", alias="thermalFraction")
    throttle_cause: Optional[StrictStr] = Field(default=None, description="Says in a few words what slowed the devices: \"Power limit\", which is normal under sustained full load, \"Too hot\" or \"Hardware slowdown\". Empty when nothing did or the cause is unknown.", alias="throttleCause")
    throttled_fraction: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="throttledFraction")
    utilization: Optional[Union[StrictFloat, StrictInt]] = None
    vendor: Optional[AcceleratorVendor] = Field(default=None, description="The maker of the accelerators these numbers came from; absent when the catalog does not define it.")
    xid_errors: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The TOTAL across the range, not a mean: a fault is an event that happened, not a level that held.", alias="xidErrors")
    __properties: ClassVar[List[str]] = ["devices", "hardwareSlowdownFraction", "measuredSeconds", "memoryTotalBytes", "memoryUsedBytes", "powerCapFraction", "powerWatts", "smOccupancy", "source", "temperatureCelsius", "thermalFraction", "throttleCause", "throttledFraction", "utilization", "vendor", "xidErrors"]

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
        """Create an instance of AcceleratorMetricsSummary from a JSON string"""
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
        """Create an instance of AcceleratorMetricsSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "devices": obj.get("devices"),
            "hardwareSlowdownFraction": obj.get("hardwareSlowdownFraction"),
            "measuredSeconds": obj.get("measuredSeconds"),
            "memoryTotalBytes": obj.get("memoryTotalBytes"),
            "memoryUsedBytes": obj.get("memoryUsedBytes"),
            "powerCapFraction": obj.get("powerCapFraction"),
            "powerWatts": obj.get("powerWatts"),
            "smOccupancy": obj.get("smOccupancy"),
            "source": obj.get("source"),
            "temperatureCelsius": obj.get("temperatureCelsius"),
            "thermalFraction": obj.get("thermalFraction"),
            "throttleCause": obj.get("throttleCause"),
            "throttledFraction": obj.get("throttledFraction"),
            "utilization": obj.get("utilization"),
            "vendor": obj.get("vendor"),
            "xidErrors": obj.get("xidErrors")
        })
        return _obj


