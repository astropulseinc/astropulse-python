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
from astropulse._generated.models.gpu_quota_headroom import GPUQuotaHeadroom
from astropulse._generated.models.gpu_quota_state import GPUQuotaState
from astropulse._generated.models.gpu_quota_unverified_reason import GPUQuotaUnverifiedReason
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelPlacementQuota(BaseModel):
    """
    ModelPlacementQuota
    """ # noqa: E501
    by_capacity_type: Optional[List[GPUQuotaHeadroom]] = Field(default=None, description="Each purchase option's own quota for the node, in the order the pool prefers them, when it buys more than one.", alias="byCapacityType")
    code: Optional[StrictStr] = Field(default=None, description="The quota's code, for example L-DB2E81BA.")
    in_use: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How much of the quota is already in use; absent when unverified.", alias="inUse")
    limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The quota's current value; absent when unverified.")
    message: Optional[StrictStr] = Field(default=None, description="Says the verdict in a sentence.")
    name: Optional[StrictStr] = Field(default=None, description="The quota's name, for example Running On-Demand G and VT instances.")
    required: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How much of the quota one replica's node needs; absent when unverified.")
    status: Optional[GPUQuotaState] = Field(default=None, description="Whether the quota has room for the node; Unverified, when it could not be read, never means zero.")
    unit: Optional[StrictStr] = Field(default=None, description="What the quota counts, for example vCPU.")
    unverified_reason: Optional[GPUQuotaUnverifiedReason] = Field(default=None, description="Why the quota was not read, when status is Unverified.", alias="unverifiedReason")
    __properties: ClassVar[List[str]] = ["byCapacityType", "code", "inUse", "limit", "message", "name", "required", "status", "unit", "unverifiedReason"]

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
        """Create an instance of ModelPlacementQuota from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in by_capacity_type (list)
        _items = []
        if self.by_capacity_type:
            for _item_by_capacity_type in self.by_capacity_type:
                if _item_by_capacity_type:
                    _items.append(_item_by_capacity_type.to_dict())
            _dict['byCapacityType'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelPlacementQuota from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "byCapacityType": [GPUQuotaHeadroom.from_dict(_item) for _item in obj["byCapacityType"]] if obj.get("byCapacityType") is not None else None,
            "code": obj.get("code"),
            "inUse": obj.get("inUse"),
            "limit": obj.get("limit"),
            "message": obj.get("message"),
            "name": obj.get("name"),
            "required": obj.get("required"),
            "status": obj.get("status"),
            "unit": obj.get("unit"),
            "unverifiedReason": obj.get("unverifiedReason")
        })
        return _obj


