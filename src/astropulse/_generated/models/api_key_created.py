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
from astropulse._generated.models.api_key_lifecycle_status import APIKeyLifecycleStatus
from astropulse._generated.models.api_key_source import APIKeySource
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class APIKeyCreated(BaseModel):
    """
    APIKeyCreated
    """ # noqa: E501
    created_at: Optional[StrictStr] = Field(default=None, description="The issuance timestamp.", alias="createdAt")
    duration: Optional[StrictStr] = Field(default=None, description="The configured lifetime; empty for permanent keys.")
    expires_at: Optional[StrictStr] = Field(default=None, description="The expiry timestamp; absent for permanent keys.", alias="expiresAt")
    id: Optional[StrictStr] = Field(default=None, description="Identifies this credential.")
    is_permanent: Optional[StrictBool] = Field(default=None, description="Indicates that this credential has no expiry.", alias="isPermanent")
    key: Optional[StrictStr] = Field(default=None, description="The secret API key. Store it securely now: it cannot be retrieved again.")
    last_used_at: Optional[StrictStr] = Field(default=None, description="The most recently recorded successful authentication.", alias="lastUsedAt")
    masked_key: Optional[StrictStr] = Field(default=None, description="A non-secret display representation of the credential.", alias="maskedKey")
    name: Optional[StrictStr] = Field(default=None, description="Labels this credential.")
    org_id: Optional[StrictStr] = Field(default=None, description="Identifies the organization this credential may access.", alias="orgId")
    org_namespace: Optional[StrictStr] = Field(default=None, description="The organization's short name.", alias="orgNamespace")
    revoked_at: Optional[StrictStr] = Field(default=None, description="The revocation timestamp, when revoked.", alias="revokedAt")
    revoked_by: Optional[StrictStr] = Field(default=None, description="Identifies the administrator who revoked the credential.", alias="revokedBy")
    revoked_reason: Optional[StrictStr] = Field(default=None, description="Explains why the credential was revoked.", alias="revokedReason")
    service_account_id: Optional[StrictStr] = Field(default=None, description="The service account that owns the key; absent for personal keys.", alias="serviceAccountId")
    source: Optional[APIKeySource] = Field(default=None, description="Where the key was issued: CLI, UI or Nova for a personal key, API for a service account key.")
    status: Optional[APIKeyLifecycleStatus] = Field(default=None, description="The credential lifecycle state.")
    user_id: Optional[StrictStr] = Field(default=None, description="The user who owns a personal key; empty for service-account keys.", alias="userId")
    __properties: ClassVar[List[str]] = ["createdAt", "duration", "expiresAt", "id", "isPermanent", "key", "lastUsedAt", "maskedKey", "name", "orgId", "orgNamespace", "revokedAt", "revokedBy", "revokedReason", "serviceAccountId", "source", "status", "userId"]

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
        """Create an instance of APIKeyCreated from a JSON string"""
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
        """Create an instance of APIKeyCreated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "duration": obj.get("duration"),
            "expiresAt": obj.get("expiresAt"),
            "id": obj.get("id"),
            "isPermanent": obj.get("isPermanent"),
            "key": obj.get("key"),
            "lastUsedAt": obj.get("lastUsedAt"),
            "maskedKey": obj.get("maskedKey"),
            "name": obj.get("name"),
            "orgId": obj.get("orgId"),
            "orgNamespace": obj.get("orgNamespace"),
            "revokedAt": obj.get("revokedAt"),
            "revokedBy": obj.get("revokedBy"),
            "revokedReason": obj.get("revokedReason"),
            "serviceAccountId": obj.get("serviceAccountId"),
            "source": obj.get("source"),
            "status": obj.get("status"),
            "userId": obj.get("userId")
        })
        return _obj


