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
from astropulse._generated.models.organization_role import OrganizationRole
from astropulse._generated.models.permission import Permission
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Role(BaseModel):
    """
    Role
    """ # noqa: E501
    assignable: Optional[StrictBool] = Field(default=None, description="True for the roles add-member and set-role accept. The owner role is false: it moves only by ownership transfer.")
    id: Optional[StrictStr] = Field(default=None, description="Identifies the role; the same value as `key`.")
    key: Optional[OrganizationRole] = Field(default=None, description="The value add-member and set-role take as `role`.")
    name: Optional[StrictStr] = Field(default=None, description="The role's display name.")
    permissions: Optional[List[Permission]] = Field(default=None, description="What a holder of the role may do.")
    __properties: ClassVar[List[str]] = ["assignable", "id", "key", "name", "permissions"]

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
        """Create an instance of Role from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict['permissions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Role from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assignable": obj.get("assignable"),
            "id": obj.get("id"),
            "key": obj.get("key"),
            "name": obj.get("name"),
            "permissions": [Permission.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None
        })
        return _obj


