# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.api_key_expiration import APIKeyExpiration
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class APIKeySummary(BaseModel):
    """
    APIKeySummary
    """ # noqa: E501
    active_key_count: Optional[StrictInt] = Field(default=None, description="How many keys can authenticate now.", alias="activeKeyCount")
    expired_key_count: Optional[StrictInt] = Field(default=None, description="How many keys are past their expiry.", alias="expiredKeyCount")
    nearest_expiring_key: Optional[APIKeyExpiration] = Field(default=None, description="The active key that expires first within the next 7 days; absent when none does.", alias="nearestExpiringKey")
    revoked_key_count: Optional[StrictInt] = Field(default=None, description="How many keys were revoked.", alias="revokedKeyCount")
    __properties: ClassVar[List[str]] = ["activeKeyCount", "expiredKeyCount", "nearestExpiringKey", "revokedKeyCount"]

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
        """Create an instance of APIKeySummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of nearest_expiring_key
        if self.nearest_expiring_key:
            _dict['nearestExpiringKey'] = self.nearest_expiring_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of APIKeySummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeKeyCount": obj.get("activeKeyCount"),
            "expiredKeyCount": obj.get("expiredKeyCount"),
            "nearestExpiringKey": APIKeyExpiration.from_dict(obj["nearestExpiringKey"]) if obj.get("nearestExpiringKey") is not None else None,
            "revokedKeyCount": obj.get("revokedKeyCount")
        })
        return _obj


