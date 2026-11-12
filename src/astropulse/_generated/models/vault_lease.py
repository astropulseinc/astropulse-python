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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.provisioner_type import ProvisionerType
from astropulse._generated.models.vault_lease_kind import VaultLeaseKind
from astropulse._generated.models.vault_lease_scope import VaultLeaseScope
from astropulse._generated.models.vault_lease_state import VaultLeaseState
from astropulse._generated.models.vault_validation import VaultValidation
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class VaultLease(BaseModel):
    """
    VaultLease
    """ # noqa: E501
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster a cluster-scoped credential serves.", alias="clusterName", json_schema_extra={"examples": ["prod"]})
    created_by: Optional[StrictStr] = Field(default=None, description="The user who first stored it, when known. Admins only.", alias="createdBy")
    created_by_display: Optional[StrictStr] = Field(default=None, description="Names the user who first stored it, by name and email; empty when unknown. Admins only.", alias="createdByDisplay")
    expires_at: Optional[datetime] = Field(default=None, description="When the credential expires; omitted for credentials that do not.", alias="expiresAt")
    fingerprint: Optional[StrictStr] = Field(default=None, description="A short one-way digest of the value, for telling two credentials apart. Admins only.", json_schema_extra={"examples": ["9f2c4e1a"]})
    issued_at: Optional[datetime] = Field(default=None, description="When the credential was first stored.", alias="issuedAt")
    kind: Optional[VaultLeaseKind] = Field(default=None, description="What the credential is; absent for a kind AstroPulse no longer defines.")
    last4: Optional[StrictStr] = Field(default=None, description="The value's last four characters, shown only for kinds long enough that it reveals nothing. Admins only.", json_schema_extra={"examples": ["x7Qa"]})
    last_validated: Optional[datetime] = Field(default=None, description="When AstroPulse last checked the credential with its provider.", alias="lastValidated")
    last_validation: Optional[VaultValidation] = Field(default=None, description="What that check found; omitted until one has run.", alias="lastValidation")
    last_written_by: Optional[StrictStr] = Field(default=None, description="The user who wrote it last, when known. Admins only.", alias="lastWrittenBy")
    last_written_by_display: Optional[StrictStr] = Field(default=None, description="Names the user who wrote it last, by name and email; empty when unknown. Admins only.", alias="lastWrittenByDisplay")
    lease_id: Optional[StrictStr] = Field(default=None, description="Identifies this credential; storing a different value issues a new one. Admins only.", alias="leaseId", json_schema_extra={"examples": ["3f6c1b9e-2d4a-4f8e-9b1c-7a5d2e8f0c13"]})
    name: Optional[StrictStr] = Field(default=None, description="A named credential's name, such as a registry or provider.", json_schema_extra={"examples": ["ghcr"]})
    path: Optional[StrictStr] = Field(default=None, description="Where the credential lives: org/<organization>/<kind>/<scope>. Admins only.", json_schema_extra={"examples": ["org/7d1e.../selfhosted-aws/prod"]})
    producer: Optional[StrictStr] = Field(default=None, description="The AstroPulse operation that stored it. Admins only.", json_schema_extra={"examples": ["selfhosted-setup"]})
    provisioner: Optional[ProvisionerType] = Field(default=None, description="The kind of cluster a cloud credential serves; omitted for other credentials.")
    provisioner_name: Optional[StrictStr] = Field(default=None, description="The provisioner's name for people, such as Amazon EKS; omitted for other credentials.", alias="provisionerName", json_schema_extra={"examples": ["Self-hosted Kubernetes"]})
    replace_command: Optional[StrictStr] = Field(default=None, description="The astroctl command that replaces the stored value, with this credential's own values filled in; empty when not replaceable or not yet known. Admins only.", alias="replaceCommand", json_schema_extra={"examples": ["astroctl cloud gcp selfHosted connect --cluster-name prod --project-id my-proj --region us-central1 --credentials <path-to-new-key.json> --replace"]})
    replace_instruction: Optional[StrictStr] = Field(default=None, description="Says in one sentence how to replace the stored value; empty when not replaceable. Admins only.", alias="replaceInstruction")
    replaceable: Optional[StrictBool] = Field(default=None, description="True when you can replace the stored value with a new one you made. Admins only.")
    rotated_at: Optional[datetime] = Field(default=None, description="When a different value last replaced the stored one.", alias="rotatedAt")
    scope: Optional[VaultLeaseScope] = Field(default=None, description="Whether it is the organization's one credential of its kind, one of several named ones, or one cluster's.")
    state: Optional[VaultLeaseState] = Field(default=None, description="Whether AstroPulse can read the stored credential.")
    title: Optional[StrictStr] = Field(default=None, description="AstroPulse's name for the credential.", json_schema_extra={"examples": ["AWS credentials for prod"]})
    updated_at: Optional[datetime] = Field(default=None, description="When anything about the credential last changed.", alias="updatedAt")
    used_for: Optional[StrictStr] = Field(default=None, description="Says in one line what the credential powers.", alias="usedFor", json_schema_extra={"examples": ["Creating, changing and repairing this cluster"]})
    version: Optional[StrictInt] = Field(default=None, description="Counts the values stored under this credential; it goes up with every rotation. Admins only.", json_schema_extra={"examples": [3]})
    __properties: ClassVar[List[str]] = ["clusterName", "createdBy", "createdByDisplay", "expiresAt", "fingerprint", "issuedAt", "kind", "last4", "lastValidated", "lastValidation", "lastWrittenBy", "lastWrittenByDisplay", "leaseId", "name", "path", "producer", "provisioner", "provisionerName", "replaceCommand", "replaceInstruction", "replaceable", "rotatedAt", "scope", "state", "title", "updatedAt", "usedFor", "version"]

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
        """Create an instance of VaultLease from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of last_validation
        if self.last_validation:
            _dict['lastValidation'] = self.last_validation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VaultLease from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "createdBy": obj.get("createdBy"),
            "createdByDisplay": obj.get("createdByDisplay"),
            "expiresAt": obj.get("expiresAt"),
            "fingerprint": obj.get("fingerprint"),
            "issuedAt": obj.get("issuedAt"),
            "kind": obj.get("kind"),
            "last4": obj.get("last4"),
            "lastValidated": obj.get("lastValidated"),
            "lastValidation": VaultValidation.from_dict(obj["lastValidation"]) if obj.get("lastValidation") is not None else None,
            "lastWrittenBy": obj.get("lastWrittenBy"),
            "lastWrittenByDisplay": obj.get("lastWrittenByDisplay"),
            "leaseId": obj.get("leaseId"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "producer": obj.get("producer"),
            "provisioner": obj.get("provisioner"),
            "provisionerName": obj.get("provisionerName"),
            "replaceCommand": obj.get("replaceCommand"),
            "replaceInstruction": obj.get("replaceInstruction"),
            "replaceable": obj.get("replaceable"),
            "rotatedAt": obj.get("rotatedAt"),
            "scope": obj.get("scope"),
            "state": obj.get("state"),
            "title": obj.get("title"),
            "updatedAt": obj.get("updatedAt"),
            "usedFor": obj.get("usedFor"),
            "version": obj.get("version")
        })
        return _obj


