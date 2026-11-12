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
from astropulse._generated.models.gpu_quota_state import GPUQuotaState
from astropulse._generated.models.gpu_quota_unverified_reason import GPUQuotaUnverifiedReason
from astropulse._generated.models.instance_type import InstanceType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GPUQuotaHeadroom(BaseModel):
    """
    GPUQuotaHeadroom
    """ # noqa: E501
    available: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How much of the quota is free now; absent when unverified.")
    capacity_type: Optional[InstanceType] = Field(default=None, description="The purchase option: OnDemand or Spot.", alias="capacityType")
    code: Optional[StrictStr] = Field(default=None, description="The quota's code, for example L-3819A6DF.")
    in_use: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How much of the quota is already in use; absent when unverified.", alias="inUse")
    limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The quota's current value; absent when unverified.")
    name: Optional[StrictStr] = Field(default=None, description="The quota's name, for example All G and VT Spot Instance Requests.")
    needed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How much of the quota one node needs; absent when unverified.")
    state: Optional[GPUQuotaState] = Field(default=None, description="Whether the quota has room for the node.")
    unit: Optional[StrictStr] = Field(default=None, description="What the quota counts: vCPU or GPU.")
    unverified_reason: Optional[GPUQuotaUnverifiedReason] = Field(default=None, description="Why the quota was not read, when state is Unverified.", alias="unverifiedReason")
    __properties: ClassVar[List[str]] = ["available", "capacityType", "code", "inUse", "limit", "name", "needed", "state", "unit", "unverifiedReason"]

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
        """Create an instance of GPUQuotaHeadroom from a JSON string"""
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
        """Create an instance of GPUQuotaHeadroom from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available": obj.get("available"),
            "capacityType": obj.get("capacityType"),
            "code": obj.get("code"),
            "inUse": obj.get("inUse"),
            "limit": obj.get("limit"),
            "name": obj.get("name"),
            "needed": obj.get("needed"),
            "state": obj.get("state"),
            "unit": obj.get("unit"),
            "unverifiedReason": obj.get("unverifiedReason")
        })
        return _obj


