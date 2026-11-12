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
from astropulse._generated.models.preflight_check import PreflightCheck
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.provisioner_type import ProvisionerType
from astropulse._generated.models.rolling_update_strategy import RollingUpdateStrategy
from astropulse._generated.models.upgrade_plan_phase import UpgradePlanPhase
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpgradePlan(BaseModel):
    """
    UpgradePlan
    """ # noqa: E501
    cluster_name: Optional[StrictStr] = Field(default=None, description="The name of the cluster being upgraded", alias="clusterName")
    current_version: Optional[StrictStr] = Field(default=None, description="The current Kubernetes version", alias="currentVersion")
    phases: Optional[List[UpgradePlanPhase]] = Field(default=None, description="Lists the upgrade phases in execution order")
    preflight_checks: Optional[List[PreflightCheck]] = Field(default=None, description="Contains automated validation checks run before the upgrade", alias="preflightChecks")
    provider: Optional[Provider] = Field(default=None, description="The cloud the cluster runs in.")
    provisioner_type: Optional[ProvisionerType] = Field(default=None, description="What created and manages the cluster.", alias="provisionerType")
    region: Optional[StrictStr] = Field(default=None, description="The cloud provider region")
    rolling_strategy: Optional[RollingUpdateStrategy] = Field(default=None, description="Describes how existing nodes are replaced; absent when the update only creates node groups.", alias="rollingStrategy")
    target_version: Optional[StrictStr] = Field(default=None, description="The target Kubernetes version", alias="targetVersion")
    unfinished_checks: Optional[List[StrictStr]] = Field(default=None, description="Names the checks that did not finish, so they neither passed nor failed; run the dry run again.", alias="unfinishedChecks")
    __properties: ClassVar[List[str]] = ["clusterName", "currentVersion", "phases", "preflightChecks", "provider", "provisionerType", "region", "rollingStrategy", "targetVersion", "unfinishedChecks"]

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
        """Create an instance of UpgradePlan from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in phases (list)
        _items = []
        if self.phases:
            for _item_phases in self.phases:
                if _item_phases:
                    _items.append(_item_phases.to_dict())
            _dict['phases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in preflight_checks (list)
        _items = []
        if self.preflight_checks:
            for _item_preflight_checks in self.preflight_checks:
                if _item_preflight_checks:
                    _items.append(_item_preflight_checks.to_dict())
            _dict['preflightChecks'] = _items
        # override the default output from pydantic by calling `to_dict()` of rolling_strategy
        if self.rolling_strategy:
            _dict['rollingStrategy'] = self.rolling_strategy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpgradePlan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "currentVersion": obj.get("currentVersion"),
            "phases": [UpgradePlanPhase.from_dict(_item) for _item in obj["phases"]] if obj.get("phases") is not None else None,
            "preflightChecks": [PreflightCheck.from_dict(_item) for _item in obj["preflightChecks"]] if obj.get("preflightChecks") is not None else None,
            "provider": obj.get("provider"),
            "provisionerType": obj.get("provisionerType"),
            "region": obj.get("region"),
            "rollingStrategy": RollingUpdateStrategy.from_dict(obj["rollingStrategy"]) if obj.get("rollingStrategy") is not None else None,
            "targetVersion": obj.get("targetVersion"),
            "unfinishedChecks": obj.get("unfinishedChecks")
        })
        return _obj


