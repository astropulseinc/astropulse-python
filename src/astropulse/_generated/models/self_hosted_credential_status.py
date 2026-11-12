# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.failure import Failure
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.self_hosted_credential_state import SelfHostedCredentialState
from astropulse._generated.models.vault_validation import VaultValidation
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SelfHostedCredentialStatus(BaseModel):
    """
    SelfHostedCredentialStatus
    """ # noqa: E501
    error: Optional[Failure] = Field(default=None, description="Contains any error message if the request failed")
    key_id: Optional[StrictStr] = Field(default=None, description="Identifies the stored key without revealing it: the AWS access key ID or the GCP service account key ID.", alias="keyId", json_schema_extra={"examples": ["0123456789abcdef0123456789abcdef01234567"]})
    last_validated: Optional[datetime] = Field(default=None, description="When AstroPulse last checked the stored credentials with the cloud provider, in RFC 3339.", alias="lastValidated")
    last_validation: Optional[VaultValidation] = Field(default=None, description="What that check found; omitted until one has run.", alias="lastValidation")
    message: Optional[StrictStr] = Field(default=None, description="Says in one sentence what the status means for the cluster and what to do next.")
    note: Optional[StrictStr] = Field(default=None, description="Says how long the key stays valid, how to rotate it, and what revoking it here leaves in the cloud account.")
    provider: Optional[Provider] = Field(default=None, description="The cloud the stored credentials are for: `aws` or `gcp`.")
    service_account: Optional[StrictStr] = Field(default=None, description="The GCP service account the stored key belongs to.", alias="serviceAccount", json_schema_extra={"examples": ["prod-1a2b3c@my-project.iam.gserviceaccount.com"]})
    status: Optional[SelfHostedCredentialState] = Field(default=None, description="How the stored credentials stand.")
    stored_at: Optional[datetime] = Field(default=None, description="When AstroPulse stored the current key, in RFC 3339.", alias="storedAt")
    vault_type: Optional[StrictStr] = Field(default=None, description="The type of credential storage", alias="vaultType")
    __properties: ClassVar[List[str]] = ["error", "keyId", "lastValidated", "lastValidation", "message", "note", "provider", "serviceAccount", "status", "storedAt", "vaultType"]

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
        """Create an instance of SelfHostedCredentialStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_validation
        if self.last_validation:
            _dict['lastValidation'] = self.last_validation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SelfHostedCredentialStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "error": Failure.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "keyId": obj.get("keyId"),
            "lastValidated": obj.get("lastValidated"),
            "lastValidation": VaultValidation.from_dict(obj["lastValidation"]) if obj.get("lastValidation") is not None else None,
            "message": obj.get("message"),
            "note": obj.get("note"),
            "provider": obj.get("provider"),
            "serviceAccount": obj.get("serviceAccount"),
            "status": obj.get("status"),
            "storedAt": obj.get("storedAt"),
            "vaultType": obj.get("vaultType")
        })
        return _obj


