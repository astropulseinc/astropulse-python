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
from astropulse._generated.models.organization import Organization
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UserProfile(BaseModel):
    """
    UserProfile
    """ # noqa: E501
    created_at: Optional[StrictStr] = Field(default=None, description="The timestamp when the user account was created (RFC 3339 format)", alias="createdAt")
    current_org_id: Optional[StrictStr] = Field(default=None, description="The user's currently active organization ID", alias="currentOrgId")
    email: Optional[StrictStr] = Field(default=None, description="The user's email address")
    identity_provider: Optional[StrictStr] = Field(default=None, description="The sign-in method the user registered with.", alias="identityProvider")
    login_count: Optional[StrictInt] = Field(default=None, description="The total number of times the user has logged in", alias="loginCount")
    name: Optional[StrictStr] = Field(default=None, description="The user's display name")
    organization: Optional[List[Organization]] = Field(default=None, description="Contains all organizations the user belongs to")
    preferred_organization_id: Optional[StrictStr] = Field(default=None, description="The user's default organization ID", alias="preferredOrganizationId")
    roles: Optional[List[StrictStr]] = Field(default=None, description="The list of roles assigned to the user")
    user_id: Optional[StrictStr] = Field(default=None, description="The unique user identifier (UUID format)", alias="userId")
    __properties: ClassVar[List[str]] = ["createdAt", "currentOrgId", "email", "identityProvider", "loginCount", "name", "organization", "preferredOrganizationId", "roles", "userId"]

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
        """Create an instance of UserProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in organization (list)
        _items = []
        if self.organization:
            for _item_organization in self.organization:
                if _item_organization:
                    _items.append(_item_organization.to_dict())
            _dict['organization'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "currentOrgId": obj.get("currentOrgId"),
            "email": obj.get("email"),
            "identityProvider": obj.get("identityProvider"),
            "loginCount": obj.get("loginCount"),
            "name": obj.get("name"),
            "organization": [Organization.from_dict(_item) for _item in obj["organization"]] if obj.get("organization") is not None else None,
            "preferredOrganizationId": obj.get("preferredOrganizationId"),
            "roles": obj.get("roles"),
            "userId": obj.get("userId")
        })
        return _obj


