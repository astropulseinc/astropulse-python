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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationResumePlan(BaseModel):
    """
    ApplicationResumePlan
    """ # noqa: E501
    application_name: Optional[StrictStr] = Field(default=None, description="The user-facing application name.", alias="applicationName")
    configured_ref: Optional[StrictStr] = Field(default=None, description="The branch/tag the app would resume tracking (e.g. \"main\").", alias="configuredRef")
    current_resolved_ref: Optional[StrictStr] = Field(default=None, description="The configured ref resolved to its current immutable revision.", alias="currentResolvedRef")
    diff: Optional[List[DeploymentDiffItem]] = Field(default=None, description="The sanitized pinned→current change summary.")
    next_actions: Optional[List[StrictStr]] = Field(default=None, description="Concrete follow-up commands for humans/automation.", alias="nextActions")
    pinned_revision: Optional[StrictStr] = Field(default=None, description="The immutable revision the app is pinned to.", alias="pinnedRevision")
    pinned_version: Optional[StrictStr] = Field(default=None, description="The Astro version currently pinned by rollback.", alias="pinnedVersion")
    requires_confirmation: Optional[StrictBool] = Field(default=None, description="Indicates a mutating apply needs confirmation (or --yes).", alias="requiresConfirmation")
    summary: Optional[StrictStr] = Field(default=None, description="Says in plain words what resuming does: the ref the application tracks again and the version it is pinned at. Empty when there is nothing to resume.")
    warnings: Optional[List[StrictStr]] = Field(default=None, description="Carries non-fatal advisories.")
    __properties: ClassVar[List[str]] = ["applicationName", "configuredRef", "currentResolvedRef", "diff", "nextActions", "pinnedRevision", "pinnedVersion", "requiresConfirmation", "summary", "warnings"]

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
        """Create an instance of ApplicationResumePlan from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationResumePlan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationName": obj.get("applicationName"),
            "configuredRef": obj.get("configuredRef"),
            "currentResolvedRef": obj.get("currentResolvedRef"),
            "diff": [DeploymentDiffItem.from_dict(_item) for _item in obj["diff"]] if obj.get("diff") is not None else None,
            "nextActions": obj.get("nextActions"),
            "pinnedRevision": obj.get("pinnedRevision"),
            "pinnedVersion": obj.get("pinnedVersion"),
            "requiresConfirmation": obj.get("requiresConfirmation"),
            "summary": obj.get("summary"),
            "warnings": obj.get("warnings")
        })
        return _obj


