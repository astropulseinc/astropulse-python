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
from astropulse._generated.models.organization_member import OrganizationMember
from astropulse._generated.models.pagination import Pagination
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class OrganizationMembersPage(BaseModel):
    """
    OrganizationMembersPage
    """ # noqa: E501
    next_page_token: Optional[StrictStr] = Field(default=None, description="Continues the listing when passed back as pageToken; empty on the last page.", alias="nextPageToken")
    pagination: Optional[Pagination] = Field(default=None, description="Where this page is in the whole list.")
    users: Optional[List[OrganizationMember]] = Field(default=None, description="The members on this page.")
    __properties: ClassVar[List[str]] = ["nextPageToken", "pagination", "users"]

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
        """Create an instance of OrganizationMembersPage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item_users in self.users:
                if _item_users:
                    _items.append(_item_users.to_dict())
            _dict['users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganizationMembersPage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nextPageToken": obj.get("nextPageToken"),
            "pagination": Pagination.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "users": [OrganizationMember.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None
        })
        return _obj


