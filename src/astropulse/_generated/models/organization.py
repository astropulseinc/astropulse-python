# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.member import Member
from astropulse._generated.models.org_feature_flags import OrgFeatureFlags
from astropulse._generated.models.organization_role import OrganizationRole
from astropulse._generated.models.plan_id import PlanId
from astropulse._generated.models.role import Role
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Organization(BaseModel):
    """
    Organization
    """ # noqa: E501
    created_at: Optional[StrictStr] = Field(default=None, description="When the organization was created.", alias="createdAt")
    feature_flags: Optional[OrgFeatureFlags] = Field(default=None, description="The features turned on for the organization.", alias="featureFlags")
    id: Optional[StrictStr] = Field(default=None, description="Identifies the organization.")
    is_default: Optional[StrictBool] = Field(default=None, description="True for your default organization, the one AstroPulse created when you signed up.", alias="isDefault")
    members: Optional[List[Member]] = Field(default=None, description="The organization's members, returned only to an admin or owner and empty otherwise. A list of organizations may hold only your own entry.")
    name: Optional[StrictStr] = Field(default=None, description="The organization's unique name.")
    org_namespace: Optional[StrictStr] = Field(default=None, description="The Kubernetes namespace that holds the organization's resources.", alias="orgNamespace")
    owner: Optional[StrictBool] = Field(default=None, description="Whether you own this organization.")
    owner_user_id: Optional[StrictStr] = Field(default=None, description="The user ID of this organization's owner. The organization routes return it only to an admin or owner.", alias="ownerUserId")
    plan_id: Optional[PlanId] = Field(default=None, description="The organization's plan.", alias="planId")
    roles: Optional[List[Role]] = Field(default=None, description="The organization's roles.")
    slug: Optional[StrictStr] = Field(default=None, description="The URL-safe form of the name.")
    title: Optional[StrictStr] = Field(default=None, description="The organization's display title.")
    user_role: Optional[OrganizationRole] = Field(default=None, description="Your role in this organization; absent when you hold none.", alias="userRole")
    __properties: ClassVar[List[str]] = ["createdAt", "featureFlags", "id", "isDefault", "members", "name", "orgNamespace", "owner", "ownerUserId", "planId", "roles", "slug", "title", "userRole"]

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
        """Create an instance of Organization from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of feature_flags
        if self.feature_flags:
            _dict['featureFlags'] = self.feature_flags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item_members in self.members:
                if _item_members:
                    _items.append(_item_members.to_dict())
            _dict['members'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item_roles in self.roles:
                if _item_roles:
                    _items.append(_item_roles.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Organization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "featureFlags": OrgFeatureFlags.from_dict(obj["featureFlags"]) if obj.get("featureFlags") is not None else None,
            "id": obj.get("id"),
            "isDefault": obj.get("isDefault"),
            "members": [Member.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None,
            "name": obj.get("name"),
            "orgNamespace": obj.get("orgNamespace"),
            "owner": obj.get("owner"),
            "ownerUserId": obj.get("ownerUserId"),
            "planId": obj.get("planId"),
            "roles": [Role.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "slug": obj.get("slug"),
            "title": obj.get("title"),
            "userRole": obj.get("userRole")
        })
        return _obj


