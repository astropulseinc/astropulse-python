# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.accelerator_vendor import AcceleratorVendor
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GPUAttachment(BaseModel):
    """
    GPUAttachment
    """ # noqa: E501
    count_per_node: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="How many devices each node carries (required, >= 1). The accelerator catalog lists the valid counts for a given model in its countsPerNode field.", alias="countPerNode")
    model: Annotated[str, Field(min_length=1, strict=True, max_length=60)] = Field(description="The required normalized model (e.g. \"l4\", \"a100\", \"mi300x\") — exactly the vocabulary the machine catalog and its filters use.")
    provider_type: Optional[StrictStr] = Field(default=None, description="The provider-native accelerator identifier AstroPulse RESOLVED for this attachment (GCP's guestAccelerator type, e.g. \"nvidia-l4\"); empty on providers whose machine type already determines the device (AWS, Azure). Read-only: it is a plan output recorded for auditability, never user input — a value sent on create or update is ignored and re-resolved from the catalog.", alias="providerType")
    vendor: Optional[AcceleratorVendor] = Field(default=None, description="The device's maker, for when the model alone is ambiguous.")
    __properties: ClassVar[List[str]] = ["countPerNode", "model", "providerType", "vendor"]

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
        """Create an instance of GPUAttachment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "provider_type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GPUAttachment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "countPerNode": obj.get("countPerNode"),
            "model": obj.get("model"),
            "providerType": obj.get("providerType"),
            "vendor": obj.get("vendor")
        })
        return _obj


