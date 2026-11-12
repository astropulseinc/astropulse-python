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
from astropulse._generated.models.hugging_face_integration_state import HuggingFaceIntegrationState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class HuggingFaceIntegration(BaseModel):
    """
    HuggingFaceIntegration
    """ # noqa: E501
    connected: Optional[StrictBool] = Field(default=None, description="Reports whether a usable token is stored for the organization.")
    connected_by: Optional[StrictStr] = Field(default=None, description="The user who connected the current token. Admins only.", alias="connectedBy")
    connected_by_display: Optional[StrictStr] = Field(default=None, description="Names that user, by name and email; empty when unknown. Admins only.", alias="connectedByDisplay")
    message: Optional[StrictStr] = Field(default=None, description="Says what to do when the state needs action; empty otherwise.")
    state: Optional[HuggingFaceIntegrationState] = Field(default=None, description="How the organization's token stands. A token that can't be read is used by nothing until it is revoked and connected again.")
    token_fingerprint: Optional[StrictStr] = Field(default=None, description="The last four characters of the stored token; empty when not connected, and omitted for callers who are not organization admins.", alias="tokenFingerprint")
    updated_at: Optional[StrictStr] = Field(default=None, description="When the token was last connected or rotated (RFC 3339); empty when not connected.", alias="updatedAt")
    verified_at: Optional[StrictStr] = Field(default=None, description="When Hugging Face last accepted the token (RFC 3339). A token is stored only after Hugging Face accepts it.", alias="verifiedAt")
    __properties: ClassVar[List[str]] = ["connected", "connectedBy", "connectedByDisplay", "message", "state", "tokenFingerprint", "updatedAt", "verifiedAt"]

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
        """Create an instance of HuggingFaceIntegration from a JSON string"""
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
        """Create an instance of HuggingFaceIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connected": obj.get("connected"),
            "connectedBy": obj.get("connectedBy"),
            "connectedByDisplay": obj.get("connectedByDisplay"),
            "message": obj.get("message"),
            "state": obj.get("state"),
            "tokenFingerprint": obj.get("tokenFingerprint"),
            "updatedAt": obj.get("updatedAt"),
            "verifiedAt": obj.get("verifiedAt")
        })
        return _obj


