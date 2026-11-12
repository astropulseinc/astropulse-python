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
from astropulse._generated.models.application_version_state import ApplicationVersionState
from astropulse._generated.models.source_identity import SourceIdentity
from astropulse._generated.models.source_type import SourceType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationVersionEntry(BaseModel):
    """
    ApplicationVersionEntry
    """ # noqa: E501
    created_at: Optional[StrictStr] = Field(default=None, description="The RFC3339 creation timestamp of the version.", alias="createdAt")
    created_by: Optional[StrictStr] = Field(default=None, description="The actor (user id) who created the version.", alias="createdBy")
    created_by_display: Optional[StrictStr] = Field(default=None, description="The human-readable actor (name, falling back to email) resolved from CreatedBy, so the whole team can see WHO deployed/rolled back rather than a raw id. Best-effort: empty when the actor cannot be resolved. Org-scoped (the actor is an org member), so this does not leak identities across organizations.", alias="createdByDisplay")
    current: Optional[StrictBool] = Field(default=None, description="Indicates this version is the currently deployed desired state.")
    rollback_eligible: Optional[StrictBool] = Field(default=None, description="Indicates whether this version can be rolled back to today.", alias="rollbackEligible")
    rollback_pinned: Optional[StrictBool] = Field(default=None, description="Indicates the current version is held by a rollback pin (git moving-ref case).", alias="rollbackPinned")
    source_identity: Optional[SourceIdentity] = Field(default=None, description="The immutable artifact identity for this version.", alias="sourceIdentity")
    source_summary: Optional[StrictStr] = Field(default=None, description="A short human-readable summary of the source.", alias="sourceSummary")
    source_type: Optional[SourceType] = Field(default=None, description="The source type for this version.", alias="sourceType")
    state: Optional[ApplicationVersionState] = Field(default=None, description="The version lifecycle state.")
    unavailable_reason: Optional[StrictStr] = Field(default=None, description="Explains why a non-eligible version cannot be rolled back to; set whenever rollbackEligible is false.", alias="unavailableReason")
    version: Optional[StrictStr] = Field(default=None, description="The Astro version label, e.g. \"v7\".")
    __properties: ClassVar[List[str]] = ["createdAt", "createdBy", "createdByDisplay", "current", "rollbackEligible", "rollbackPinned", "sourceIdentity", "sourceSummary", "sourceType", "state", "unavailableReason", "version"]

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
        """Create an instance of ApplicationVersionEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_identity
        if self.source_identity:
            _dict['sourceIdentity'] = self.source_identity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationVersionEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "createdBy": obj.get("createdBy"),
            "createdByDisplay": obj.get("createdByDisplay"),
            "current": obj.get("current"),
            "rollbackEligible": obj.get("rollbackEligible"),
            "rollbackPinned": obj.get("rollbackPinned"),
            "sourceIdentity": SourceIdentity.from_dict(obj["sourceIdentity"]) if obj.get("sourceIdentity") is not None else None,
            "sourceSummary": obj.get("sourceSummary"),
            "sourceType": obj.get("sourceType"),
            "state": obj.get("state"),
            "unavailableReason": obj.get("unavailableReason"),
            "version": obj.get("version")
        })
        return _obj


