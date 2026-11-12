# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.accelerator import Accelerator
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MachineType(BaseModel):
    """
    MachineType
    """ # noqa: E501
    accelerators: Optional[List[Accelerator]] = None
    architecture: Optional[List[StrictStr]] = None
    category: Optional[StrictStr] = None
    infos: Optional[Dict[str, Any]] = None
    memory_mb: Optional[StrictInt] = Field(default=None, alias="memoryMb")
    name: Optional[StrictStr] = None
    on_demand_price_per_hour: Optional[StrictStr] = Field(default=None, alias="onDemandPricePerHour")
    os_platform: Optional[StrictStr] = Field(default=None, alias="osPlatform")
    spot_price_per_hour: Optional[StrictStr] = Field(default=None, alias="spotPricePerHour")
    time_generated: Optional[StrictStr] = Field(default=None, alias="timeGenerated")
    v_cpu: Optional[StrictInt] = Field(default=None, alias="vCPU")
    zone: Optional[StrictStr] = None
    zones: Optional[List[StrictStr]] = Field(default=None, description="Lists every zone in the region offering this machine. Populated by the region-wide (zone \"all\") view; availability differs between zones, so per-zone placement must never be assumed from a single zone.")
    __properties: ClassVar[List[str]] = ["accelerators", "architecture", "category", "infos", "memoryMb", "name", "onDemandPricePerHour", "osPlatform", "spotPricePerHour", "timeGenerated", "vCPU", "zone", "zones"]

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
        """Create an instance of MachineType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in accelerators (list)
        _items = []
        if self.accelerators:
            for _item_accelerators in self.accelerators:
                if _item_accelerators:
                    _items.append(_item_accelerators.to_dict())
            _dict['accelerators'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MachineType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerators": [Accelerator.from_dict(_item) for _item in obj["accelerators"]] if obj.get("accelerators") is not None else None,
            "architecture": obj.get("architecture"),
            "category": obj.get("category"),
            "infos": obj.get("infos"),
            "memoryMb": obj.get("memoryMb"),
            "name": obj.get("name"),
            "onDemandPricePerHour": obj.get("onDemandPricePerHour"),
            "osPlatform": obj.get("osPlatform"),
            "spotPricePerHour": obj.get("spotPricePerHour"),
            "timeGenerated": obj.get("timeGenerated"),
            "vCPU": obj.get("vCPU"),
            "zone": obj.get("zone"),
            "zones": obj.get("zones")
        })
        return _obj


