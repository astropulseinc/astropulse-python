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
from astropulse._generated.models.organization_role import OrganizationRole
from astropulse._generated.models.plan_id import PlanId
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class OrganizationMember(BaseModel):
    """
    OrganizationMember
    """ # noqa: E501
    email: Optional[StrictStr] = Field(default=None, description="The member's email address.")
    joined_at: Optional[StrictStr] = Field(default=None, description="When the member joined the organization.", alias="joinedAt")
    name: Optional[StrictStr] = Field(default=None, description="The member's name.")
    org_id: Optional[StrictStr] = Field(default=None, description="The organization's ID.", alias="orgId")
    plan_id: Optional[PlanId] = Field(default=None, description="The organization's plan.", alias="planId")
    role: Optional[OrganizationRole] = Field(default=None, description="The member's role in the organization.")
    user_id: Optional[StrictStr] = Field(default=None, description="The member's user ID.", alias="userId")
    __properties: ClassVar[List[str]] = ["email", "joinedAt", "name", "orgId", "planId", "role", "userId"]

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
        """Create an instance of OrganizationMember from a JSON string"""
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
        """Create an instance of OrganizationMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "joinedAt": obj.get("joinedAt"),
            "name": obj.get("name"),
            "orgId": obj.get("orgId"),
            "planId": obj.get("planId"),
            "role": obj.get("role"),
            "userId": obj.get("userId")
        })
        return _obj


