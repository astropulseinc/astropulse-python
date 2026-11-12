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
from astropulse._generated.models.access_policy_api_keys import AccessPolicyAPIKeys
from astropulse._generated.models.access_policy_jwt import AccessPolicyJWT
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AccessPolicySpec(BaseModel):
    """
    AccessPolicySpec
    """ # noqa: E501
    allowed_origins: Optional[List[StrictStr]] = Field(default=None, description="Websites whose pages may call endpoints that use this policy from a browser, each as an origin such as https://app.example.com. Empty means no browser access from other sites.", alias="allowedOrigins")
    api_keys: Optional[AccessPolicyAPIKeys] = Field(default=None, alias="apiKeys")
    jwt: Optional[AccessPolicyJWT] = None
    __properties: ClassVar[List[str]] = ["allowedOrigins", "apiKeys", "jwt"]

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
        """Create an instance of AccessPolicySpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of api_keys
        if self.api_keys:
            _dict['apiKeys'] = self.api_keys.to_dict()
        # override the default output from pydantic by calling `to_dict()` of jwt
        if self.jwt:
            _dict['jwt'] = self.jwt.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessPolicySpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedOrigins": obj.get("allowedOrigins"),
            "apiKeys": AccessPolicyAPIKeys.from_dict(obj["apiKeys"]) if obj.get("apiKeys") is not None else None,
            "jwt": AccessPolicyJWT.from_dict(obj["jwt"]) if obj.get("jwt") is not None else None
        })
        return _obj


