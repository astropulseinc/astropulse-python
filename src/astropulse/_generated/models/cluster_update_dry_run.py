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
from astropulse._generated.models.cluster_status import ClusterStatus
from astropulse._generated.models.dry_run_verdict import DryRunVerdict
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.outcome import Outcome
from astropulse._generated.models.upgrade_plan import UpgradePlan
from astropulse._generated.models.upgrade_readiness_report import UpgradeReadinessReport
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterUpdateDryRun(BaseModel):
    """
    ClusterUpdateDryRun
    """ # noqa: E501
    cluster_id: Optional[StrictStr] = Field(default=None, description="The unique cluster identifier", alias="clusterId")
    errors: Optional[List[StrictStr]] = Field(default=None, description="Contains validation error messages that block the update.")
    message: Optional[StrictStr] = Field(default=None, description="Provides human-readable details about the result")
    notices: Optional[List[Notice]] = Field(default=None, description="What the update will do, what an update sent with replaceRunning does, and warnings about the cluster it leaves; a warning doesn't stop the update.")
    outcome: Optional[Outcome] = Field(default=None, description="The decision on the update: Proceed, or Blocked when a check failed or did not finish.")
    status: Optional[ClusterStatus] = Field(default=None, description="The cluster's current status.")
    title: StrictStr = Field(description="The verdict as a headline to show.")
    upgrade_plan: Optional[UpgradePlan] = Field(default=None, description="Describes the phased execution plan", alias="upgradePlan")
    upgrade_report: Optional[UpgradeReadinessReport] = Field(default=None, description="Contains a comprehensive readiness analysis (present when generateReport is true)", alias="upgradeReport")
    validation_passed: Optional[StrictBool] = Field(default=None, description="True when every check finished and none failed.", alias="validationPassed")
    verdict: DryRunVerdict = Field(description="How the dry run ended.")
    __properties: ClassVar[List[str]] = ["clusterId", "errors", "message", "notices", "outcome", "status", "title", "upgradePlan", "upgradeReport", "validationPassed", "verdict"]

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
        """Create an instance of ClusterUpdateDryRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        # override the default output from pydantic by calling `to_dict()` of upgrade_plan
        if self.upgrade_plan:
            _dict['upgradePlan'] = self.upgrade_plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of upgrade_report
        if self.upgrade_report:
            _dict['upgradeReport'] = self.upgrade_report.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterUpdateDryRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "errors": obj.get("errors"),
            "message": obj.get("message"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "outcome": obj.get("outcome"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "upgradePlan": UpgradePlan.from_dict(obj["upgradePlan"]) if obj.get("upgradePlan") is not None else None,
            "upgradeReport": UpgradeReadinessReport.from_dict(obj["upgradeReport"]) if obj.get("upgradeReport") is not None else None,
            "validationPassed": obj.get("validationPassed"),
            "verdict": obj.get("verdict")
        })
        return _obj


