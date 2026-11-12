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
from astropulse._generated.models.domain_binding_status import DomainBindingStatus
from astropulse._generated.models.domain_hostname_source import DomainHostnameSource
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class DomainBinding(BaseModel):
    """
    DomainBinding
    """ # noqa: E501
    app_name: Optional[StrictStr] = Field(default=None, description="The application the hostname serves.", alias="appName")
    created_at: Optional[datetime] = Field(default=None, description="When the hostname was bound.", alias="createdAt")
    failure_reason: Optional[StrictStr] = Field(default=None, description="Why the binding failed; absent unless it did.", alias="failureReason")
    hostname: Optional[StrictStr] = Field(default=None, description="The bound hostname.")
    hostname_source: Optional[DomainHostnameSource] = Field(default=None, description="Where the hostname came from.", alias="hostnameSource")
    status: Optional[DomainBindingStatus] = Field(default=None, description="Whether the hostname serves the application yet.")
    updated_at: Optional[datetime] = Field(default=None, description="When the binding last changed.", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["appName", "createdAt", "failureReason", "hostname", "hostnameSource", "status", "updatedAt"]

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
        """Create an instance of DomainBinding from a JSON string"""
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
        """Create an instance of DomainBinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appName": obj.get("appName"),
            "createdAt": obj.get("createdAt"),
            "failureReason": obj.get("failureReason"),
            "hostname": obj.get("hostname"),
            "hostnameSource": obj.get("hostnameSource"),
            "status": obj.get("status"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


