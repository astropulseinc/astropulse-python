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
from astropulse._generated.models.deployment_diff_item import DeploymentDiffItem
from astropulse._generated.models.source_identity import SourceIdentity
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationRollbackPlan(BaseModel):
    """
    ApplicationRollbackPlan
    """ # noqa: E501
    application_name: Optional[StrictStr] = Field(default=None, description="The user-facing application name.", alias="applicationName")
    applied_version: Optional[StrictStr] = Field(default=None, description="The newest version applied, set only when it did not finish deploying.", alias="appliedVersion")
    current_version: Optional[StrictStr] = Field(default=None, description="The version last confirmed running, as listed in the application's history.", alias="currentVersion")
    diff: Optional[List[DeploymentDiffItem]] = Field(default=None, description="The sanitized current→target change summary.")
    eligible: Optional[StrictBool] = Field(default=None, description="Indicates the rollback can proceed.")
    next_actions: Optional[List[StrictStr]] = Field(default=None, description="Concrete follow-up commands for humans/automation.", alias="nextActions")
    pinned_after_rollback: Optional[StrictBool] = Field(default=None, description="Indicates the rollback will leave the application in RollbackPinned until it is resumed.", alias="pinnedAfterRollback")
    requires_confirmation: Optional[StrictBool] = Field(default=None, description="Indicates a mutating apply needs confirmation (or --yes).", alias="requiresConfirmation")
    target_source_identity: Optional[SourceIdentity] = Field(default=None, description="The immutable identity that would be deployed.", alias="targetSourceIdentity")
    target_version: Optional[StrictStr] = Field(default=None, description="The Astro version that would be rolled back to.", alias="targetVersion")
    title: Optional[StrictStr] = Field(default=None, description="The plan's verdict as a headline to show.")
    unavailable_reason: Optional[StrictStr] = Field(default=None, description="Explains why an ineligible rollback cannot proceed.", alias="unavailableReason")
    warnings: Optional[List[StrictStr]] = Field(default=None, description="Carries non-fatal advisories (e.g. profile drift, current sync OutOfSync).")
    __properties: ClassVar[List[str]] = ["applicationName", "appliedVersion", "currentVersion", "diff", "eligible", "nextActions", "pinnedAfterRollback", "requiresConfirmation", "targetSourceIdentity", "targetVersion", "title", "unavailableReason", "warnings"]

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
        """Create an instance of ApplicationRollbackPlan from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in diff (list)
        _items = []
        if self.diff:
            for _item_diff in self.diff:
                if _item_diff:
                    _items.append(_item_diff.to_dict())
            _dict['diff'] = _items
        # override the default output from pydantic by calling `to_dict()` of target_source_identity
        if self.target_source_identity:
            _dict['targetSourceIdentity'] = self.target_source_identity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationRollbackPlan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationName": obj.get("applicationName"),
            "appliedVersion": obj.get("appliedVersion"),
            "currentVersion": obj.get("currentVersion"),
            "diff": [DeploymentDiffItem.from_dict(_item) for _item in obj["diff"]] if obj.get("diff") is not None else None,
            "eligible": obj.get("eligible"),
            "nextActions": obj.get("nextActions"),
            "pinnedAfterRollback": obj.get("pinnedAfterRollback"),
            "requiresConfirmation": obj.get("requiresConfirmation"),
            "targetSourceIdentity": SourceIdentity.from_dict(obj["targetSourceIdentity"]) if obj.get("targetSourceIdentity") is not None else None,
            "targetVersion": obj.get("targetVersion"),
            "title": obj.get("title"),
            "unavailableReason": obj.get("unavailableReason"),
            "warnings": obj.get("warnings")
        })
        return _obj


