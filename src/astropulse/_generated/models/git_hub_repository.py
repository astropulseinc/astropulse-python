# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GitHubRepository(BaseModel):
    """
    GitHubRepository
    """ # noqa: E501
    default_branch: Optional[StrictStr] = Field(default=None, json_schema_extra={"examples": ["main"]})
    description: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = Field(default=None, json_schema_extra={"examples": ["acme/api"]})
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    permissions: Optional[Dict[str, StrictBool]] = Field(default=None, description="Maps each GitHub permission (admin, maintain, push, triage, pull) to whether it is granted.")
    private: Optional[StrictBool] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["default_branch", "description", "full_name", "html_url", "id", "name", "permissions", "private", "updated_at"]

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
        """Create an instance of GitHubRepository from a JSON string"""
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
        """Create an instance of GitHubRepository from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default_branch": obj.get("default_branch"),
            "description": obj.get("description"),
            "full_name": obj.get("full_name"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "permissions": obj.get("permissions"),
            "private": obj.get("private"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


