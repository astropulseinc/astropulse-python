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
from astropulse._generated.models.git_hub_account_type import GitHubAccountType
from astropulse._generated.models.git_hub_installation_status import GitHubInstallationStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GitHubInstallation(BaseModel):
    """
    GitHubInstallation
    """ # noqa: E501
    account_id: Optional[StrictStr] = Field(default=None, description="The ID of the GitHub account the installation is on.", alias="accountId")
    account_login: Optional[StrictStr] = Field(default=None, description="The login of the GitHub account the installation is on.", alias="accountLogin")
    account_type: Optional[GitHubAccountType] = Field(default=None, description="Whether the installation is on a personal account or an organization.", alias="accountType")
    created_at: Optional[StrictStr] = Field(default=None, description="When the installation was first linked.", alias="createdAt")
    created_by_user_id: Optional[StrictStr] = Field(default=None, description="The user who linked the installation.", alias="createdByUserId")
    id: Optional[StrictStr] = Field(default=None, description="The installation's ID on GitHub.")
    linked_elsewhere: Optional[StrictBool] = Field(default=None, description="Whether the installation is also linked to at least one other organization.", alias="linkedElsewhere")
    organization_id: Optional[StrictStr] = Field(default=None, description="The organization the installation is linked to.", alias="organizationId")
    status: Optional[GitHubInstallationStatus] = Field(default=None, description="Whether the installation can be used.")
    suspended_at: Optional[StrictStr] = Field(default=None, description="When GitHub suspended the installation, if it is suspended.", alias="suspendedAt")
    updated_at: Optional[StrictStr] = Field(default=None, description="When the installation was last changed.", alias="updatedAt")
    updated_by_user_id: Optional[StrictStr] = Field(default=None, description="The user who last changed the installation.", alias="updatedByUserId")
    __properties: ClassVar[List[str]] = ["accountId", "accountLogin", "accountType", "createdAt", "createdByUserId", "id", "linkedElsewhere", "organizationId", "status", "suspendedAt", "updatedAt", "updatedByUserId"]

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
        """Create an instance of GitHubInstallation from a JSON string"""
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
        """Create an instance of GitHubInstallation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "accountLogin": obj.get("accountLogin"),
            "accountType": obj.get("accountType"),
            "createdAt": obj.get("createdAt"),
            "createdByUserId": obj.get("createdByUserId"),
            "id": obj.get("id"),
            "linkedElsewhere": obj.get("linkedElsewhere"),
            "organizationId": obj.get("organizationId"),
            "status": obj.get("status"),
            "suspendedAt": obj.get("suspendedAt"),
            "updatedAt": obj.get("updatedAt"),
            "updatedByUserId": obj.get("updatedByUserId")
        })
        return _obj


