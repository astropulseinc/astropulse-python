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
from astropulse._generated.models.access_policy_claim import AccessPolicyClaim
from astropulse._generated.models.access_policy_identity import AccessPolicyIdentity
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AccessPolicyJWT(BaseModel):
    """
    AccessPolicyJWT
    """ # noqa: E501
    audiences: Optional[List[StrictStr]] = Field(default=None, description="The aud values accepted; a token must carry at least one.")
    identity: Optional[AccessPolicyIdentity] = None
    issuer: Optional[StrictStr] = Field(default=None, description="The provider's issuer URL, exactly as its tokens carry it in iss.")
    jwks_uri: Optional[StrictStr] = Field(default=None, description="The provider's key set URL. Leave it empty to use the one the issuer's discovery document names.", alias="jwksUri")
    require: Optional[List[AccessPolicyClaim]] = Field(default=None, description="Lists claims a token must carry, each with the values accepted.")
    __properties: ClassVar[List[str]] = ["audiences", "identity", "issuer", "jwksUri", "require"]

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
        """Create an instance of AccessPolicyJWT from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in require (list)
        _items = []
        if self.require:
            for _item_require in self.require:
                if _item_require:
                    _items.append(_item_require.to_dict())
            _dict['require'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessPolicyJWT from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "audiences": obj.get("audiences"),
            "identity": AccessPolicyIdentity.from_dict(obj["identity"]) if obj.get("identity") is not None else None,
            "issuer": obj.get("issuer"),
            "jwksUri": obj.get("jwksUri"),
            "require": [AccessPolicyClaim.from_dict(_item) for _item in obj["require"]] if obj.get("require") is not None else None
        })
        return _obj


