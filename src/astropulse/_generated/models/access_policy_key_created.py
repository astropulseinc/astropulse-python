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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AccessPolicyKeyCreated(BaseModel):
    """
    AccessPolicyKeyCreated
    """ # noqa: E501
    created_at: Optional[StrictStr] = Field(default=None, description="When the key was created.", alias="createdAt")
    expires_at: Optional[StrictStr] = Field(default=None, description="When the key stops working; absent for a key that does not expire.", alias="expiresAt")
    id: Optional[StrictStr] = Field(default=None, description="Identifies the key; revoke it by this ID.")
    key: Optional[StrictStr] = Field(default=None, description="The value callers send. Store it now: it cannot be read again.")
    label: Optional[StrictStr] = Field(default=None, description="Names who the key is for.")
    __properties: ClassVar[List[str]] = ["createdAt", "expiresAt", "id", "key", "label"]

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
        """Create an instance of AccessPolicyKeyCreated from a JSON string"""
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
        """Create an instance of AccessPolicyKeyCreated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "expiresAt": obj.get("expiresAt"),
            "id": obj.get("id"),
            "key": obj.get("key"),
            "label": obj.get("label")
        })
        return _obj


