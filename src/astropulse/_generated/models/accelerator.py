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
from astropulse._generated.models.accelerator_kind import AcceleratorKind
from astropulse._generated.models.accelerator_vendor import AcceleratorVendor
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Accelerator(BaseModel):
    """
    Accelerator
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="How many devices one machine of this type carries.")
    description: Optional[StrictStr] = Field(default=None, description="What the device is for, in one sentence; absent for a model the catalog does not name.")
    display_name: Optional[StrictStr] = Field(default=None, description="The device's name as its maker writes it, such as NVIDIA L4; absent for a model the catalog does not name.", alias="displayName")
    kind: Optional[AcceleratorKind] = Field(default=None, description="The accelerator's class.")
    memory_mi_b: Optional[StrictInt] = Field(default=None, description="The memory on one device.", alias="memoryMiB")
    model: Optional[StrictStr] = Field(default=None, description="The normalised device name the catalog filters on: \"l4\", \"a100\", \"mi300x\".")
    provenance: Optional[StrictStr] = Field(default=None, description="Empty when every populated field was reported by the provider, and ProvenanceCurated when the curated table supplied one.")
    provider_type: Optional[StrictStr] = Field(default=None, description="The provider's own identifier for the device, where the provider names it separately from the machine type (GCP's \"nvidia-l4\"). Empty where the machine type already determines it.", alias="providerType")
    vendor: Optional[AcceleratorVendor] = Field(default=None, description="The device's maker; absent when the provider names none the catalog defines.")
    __properties: ClassVar[List[str]] = ["count", "description", "displayName", "kind", "memoryMiB", "model", "provenance", "providerType", "vendor"]

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
        """Create an instance of Accelerator from a JSON string"""
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
        """Create an instance of Accelerator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "kind": obj.get("kind"),
            "memoryMiB": obj.get("memoryMiB"),
            "model": obj.get("model"),
            "provenance": obj.get("provenance"),
            "providerType": obj.get("providerType"),
            "vendor": obj.get("vendor")
        })
        return _obj


