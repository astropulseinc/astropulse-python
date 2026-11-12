# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.domain_binding import DomainBinding
from astropulse._generated.models.domain_status import DomainStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Domain(BaseModel):
    """
    Domain
    """ # noqa: E501
    bindings: Optional[List[DomainBinding]] = Field(default=None, description="The hostnames under the domain bound to applications.")
    created_at: Optional[datetime] = Field(default=None, description="When the domain was claimed.", alias="createdAt")
    failure_reason: Optional[StrictStr] = Field(default=None, description="Why verification failed; absent unless it did.", alias="failureReason")
    id: Optional[StrictStr] = Field(default=None, description="The domain's identifier.")
    name: Optional[StrictStr] = Field(default=None, description="The domain name, such as example.com.")
    org_id: Optional[StrictStr] = Field(default=None, description="The organization that claims the domain.", alias="orgId")
    status: Optional[DomainStatus] = Field(default=None, description="How far the domain's verification has got.")
    updated_at: Optional[datetime] = Field(default=None, description="When the domain last changed.", alias="updatedAt")
    verification_expires_at: Optional[datetime] = Field(default=None, description="When the verification challenge expires.", alias="verificationExpiresAt")
    verification_record_name: Optional[StrictStr] = Field(default=None, description="The DNS name to publish the verification TXT record at.", alias="verificationRecordName")
    verification_record_value: Optional[StrictStr] = Field(default=None, description="The value the verification TXT record must hold.", alias="verificationRecordValue")
    verification_token: Optional[StrictStr] = Field(default=None, description="The token inside the verification value.", alias="verificationToken")
    verified_at: Optional[datetime] = Field(default=None, description="When the domain was verified; absent until it is.", alias="verifiedAt")
    __properties: ClassVar[List[str]] = ["bindings", "createdAt", "failureReason", "id", "name", "orgId", "status", "updatedAt", "verificationExpiresAt", "verificationRecordName", "verificationRecordValue", "verificationToken", "verifiedAt"]

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
        """Create an instance of Domain from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bindings (list)
        _items = []
        if self.bindings:
            for _item_bindings in self.bindings:
                if _item_bindings:
                    _items.append(_item_bindings.to_dict())
            _dict['bindings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Domain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bindings": [DomainBinding.from_dict(_item) for _item in obj["bindings"]] if obj.get("bindings") is not None else None,
            "createdAt": obj.get("createdAt"),
            "failureReason": obj.get("failureReason"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "orgId": obj.get("orgId"),
            "status": obj.get("status"),
            "updatedAt": obj.get("updatedAt"),
            "verificationExpiresAt": obj.get("verificationExpiresAt"),
            "verificationRecordName": obj.get("verificationRecordName"),
            "verificationRecordValue": obj.get("verificationRecordValue"),
            "verificationToken": obj.get("verificationToken"),
            "verifiedAt": obj.get("verifiedAt")
        })
        return _obj


