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
from astropulse._generated.models.dry_run_verdict import DryRunVerdict
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.preflight_check import PreflightCheck
from astropulse._generated.models.resolved_node_group import ResolvedNodeGroup
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterDryRun(BaseModel):
    """
    ClusterDryRun
    """ # noqa: E501
    checks: Optional[List[PreflightCheck]] = Field(default=None, description="The checks a create runs before it starts, the account connection first. A check whose status is Fail carries its fix in remediation; Warn does not block.")
    complete: Optional[StrictBool] = Field(default=None, description="False when some checks did not finish; unfinishedChecks names them and the dry run should be run again.")
    message: Optional[StrictStr] = Field(default=None, description="The verdict in words; it names each failed check and its fix, and any check that did not finish.")
    notices: Optional[List[Notice]] = Field(default=None, description="Warnings about the cluster the create would make; they don't stop it.")
    resolved_node_groups: Optional[List[ResolvedNodeGroup]] = Field(default=None, description="The node groups that named an accelerator but no machine type, with the machine types AstroPulse chose for them, in name order.", alias="resolvedNodeGroups")
    title: StrictStr = Field(description="The verdict as a headline to show.")
    unfinished_checks: Optional[List[StrictStr]] = Field(default=None, description="The checks that did not finish, so they neither passed nor failed.", alias="unfinishedChecks")
    valid: Optional[StrictBool] = Field(default=None, description="True when every check finished and none failed, so a create with the same body would start.")
    verdict: DryRunVerdict = Field(description="How the dry run ended.")
    __properties: ClassVar[List[str]] = ["checks", "complete", "message", "notices", "resolvedNodeGroups", "title", "unfinishedChecks", "valid", "verdict"]

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
        """Create an instance of ClusterDryRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in checks (list)
        _items = []
        if self.checks:
            for _item_checks in self.checks:
                if _item_checks:
                    _items.append(_item_checks.to_dict())
            _dict['checks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resolved_node_groups (list)
        _items = []
        if self.resolved_node_groups:
            for _item_resolved_node_groups in self.resolved_node_groups:
                if _item_resolved_node_groups:
                    _items.append(_item_resolved_node_groups.to_dict())
            _dict['resolvedNodeGroups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterDryRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "checks": [PreflightCheck.from_dict(_item) for _item in obj["checks"]] if obj.get("checks") is not None else None,
            "complete": obj.get("complete"),
            "message": obj.get("message"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "resolvedNodeGroups": [ResolvedNodeGroup.from_dict(_item) for _item in obj["resolvedNodeGroups"]] if obj.get("resolvedNodeGroups") is not None else None,
            "title": obj.get("title"),
            "unfinishedChecks": obj.get("unfinishedChecks"),
            "valid": obj.get("valid"),
            "verdict": obj.get("verdict")
        })
        return _obj


