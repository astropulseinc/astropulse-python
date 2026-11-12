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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class OrgServiceAccount(BaseModel):
    """
    OrgServiceAccount
    """ # noqa: E501
    archived_at: Optional[StrictStr] = Field(default=None, description="When the account was archived. An archived account and all its keys are disabled permanently.", alias="archivedAt")
    created_at: Optional[StrictStr] = Field(default=None, description="The creation timestamp.", alias="createdAt")
    created_by: Optional[StrictStr] = Field(default=None, description="Identifies the user who created this account.", alias="createdBy")
    description: Optional[StrictStr] = Field(default=None, description="Describes the automation.")
    id: Optional[StrictStr] = Field(default=None, description="Identifies this service account.")
    name: Optional[StrictStr] = Field(default=None, description="Labels this service account.")
    org_id: Optional[StrictStr] = Field(default=None, description="Identifies the owning organization.", alias="orgId")
    role: Optional[OrganizationRole] = Field(default=None, description="The organization's role assigned to this account.")
    __properties: ClassVar[List[str]] = ["archivedAt", "createdAt", "createdBy", "description", "id", "name", "orgId", "role"]

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
        """Create an instance of OrgServiceAccount from a JSON string"""
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
        """Create an instance of OrgServiceAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivedAt": obj.get("archivedAt"),
            "createdAt": obj.get("createdAt"),
            "createdBy": obj.get("createdBy"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "orgId": obj.get("orgId"),
            "role": obj.get("role")
        })
        return _obj


