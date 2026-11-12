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
from astropulse._generated.models.accelerator_kind import AcceleratorKind
from astropulse._generated.models.accelerator_vendor import AcceleratorVendor
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AcceleratorOffering(BaseModel):
    """
    AcceleratorOffering
    """ # noqa: E501
    age_seconds: Optional[StrictInt] = Field(default=None, description="Seconds between scrapedAt and when this answer was made; absent when scrapedAt is.", alias="ageSeconds")
    counts_per_node: Optional[List[StrictInt]] = Field(default=None, description="Distinct device counts per machine across the carriers, ascending — exactly the valid countPerNode values for a node group's accelerator request. Empty when no carrier reports a whole-device count (fractional-GPU families).", alias="countsPerNode")
    description: Optional[StrictStr] = Field(default=None, description="What the device is for, in one sentence; absent for a model the catalog does not name.")
    display_name: Optional[StrictStr] = Field(default=None, description="The device's name as its maker writes it, such as NVIDIA L4; absent for a model the catalog does not name.", alias="displayName")
    kind: Optional[AcceleratorKind] = Field(default=None, description="The accelerator's class.")
    machine_type_count: Optional[StrictInt] = Field(default=None, description="Number of machine types in the region carrying this accelerator.", alias="machineTypeCount")
    machine_types: Optional[List[StrictStr]] = Field(default=None, description="Machine types carrying this accelerator, the one behind the minimum on-demand price first, unpriced ones last.", alias="machineTypes")
    memory_mi_b: Optional[StrictInt] = Field(default=None, description="Memory per accelerator device in MiB; absent when neither the provider nor the curated table reports it.", alias="memoryMiB")
    min_on_demand_price_per_hour: Optional[StrictStr] = Field(default=None, description="Lowest hourly on-demand price among the machine types carrying it; absent when none is priced.", alias="minOnDemandPricePerHour")
    min_spot_price_per_hour: Optional[StrictStr] = Field(default=None, description="Lowest hourly spot price among the machine types carrying it; absent when none is priced.", alias="minSpotPricePerHour")
    model: Optional[StrictStr] = Field(default=None, description="The normalised device name a node group's accelerator request names: \"l4\", \"a100\", \"mi300x\".")
    refresh_failed_at: Optional[StrictStr] = Field(default=None, description="When the most recent refresh of this provider's catalog failed, RFC 3339; absent when the most recent refresh succeeded. The data shown is from scrapedAt.", alias="refreshFailedAt")
    scraped_at: Optional[StrictStr] = Field(default=None, description="When this offering's catalog data was last refreshed from the provider, RFC 3339. Provider pricing and availability may have changed since.", alias="scrapedAt")
    stale: Optional[StrictBool] = Field(default=None, description="True when the data was last refreshed more than 48 hours ago, or never. Show its prices as out of date, not current.")
    vendor: Optional[AcceleratorVendor] = Field(default=None, description="The device's maker; absent when the provider names none the catalog defines.")
    __properties: ClassVar[List[str]] = ["ageSeconds", "countsPerNode", "description", "displayName", "kind", "machineTypeCount", "machineTypes", "memoryMiB", "minOnDemandPricePerHour", "minSpotPricePerHour", "model", "refreshFailedAt", "scrapedAt", "stale", "vendor"]

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
        """Create an instance of AcceleratorOffering from a JSON string"""
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
        """Create an instance of AcceleratorOffering from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ageSeconds": obj.get("ageSeconds"),
            "countsPerNode": obj.get("countsPerNode"),
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "kind": obj.get("kind"),
            "machineTypeCount": obj.get("machineTypeCount"),
            "machineTypes": obj.get("machineTypes"),
            "memoryMiB": obj.get("memoryMiB"),
            "minOnDemandPricePerHour": obj.get("minOnDemandPricePerHour"),
            "minSpotPricePerHour": obj.get("minSpotPricePerHour"),
            "model": obj.get("model"),
            "refreshFailedAt": obj.get("refreshFailedAt"),
            "scrapedAt": obj.get("scrapedAt"),
            "stale": obj.get("stale"),
            "vendor": obj.get("vendor")
        })
        return _obj


