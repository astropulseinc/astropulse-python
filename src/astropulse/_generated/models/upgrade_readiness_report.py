# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_health_check import ClusterHealthCheck
from astropulse._generated.models.k8s_version_analysis import K8sVersionAnalysis
from astropulse._generated.models.readiness_report_section import ReadinessReportSection
from astropulse._generated.models.resource_capacity_check import ResourceCapacityCheck
from astropulse._generated.models.upgrade_risk_level import UpgradeRiskLevel
from astropulse._generated.models.validation_issue import ValidationIssue
from astropulse._generated.models.workload_impact_analysis import WorkloadImpactAnalysis
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpgradeReadinessReport(BaseModel):
    """
    UpgradeReadinessReport
    """ # noqa: E501
    can_proceed: Optional[StrictBool] = Field(default=None, description="Indicates whether the upgrade can safely proceed", alias="canProceed")
    cluster_health: Optional[ClusterHealthCheck] = Field(default=None, description="The current cluster health assessment; absent when not evaluated.", alias="clusterHealth")
    critical_issues: Optional[List[ValidationIssue]] = Field(default=None, description="Blocking issues that must be resolved before upgrading", alias="criticalIssues")
    estimated_time: Optional[StrictStr] = Field(default=None, description="The estimated upgrade duration (e.g. \"45-60 minutes\")", alias="estimatedTime")
    not_evaluated: Optional[List[ReadinessReportSection]] = Field(default=None, description="Names the analysis sections this report does not include.", alias="notEvaluated")
    nothing_to_upgrade: Optional[StrictBool] = Field(default=None, description="True when the cluster is already at the newest version the requested target resolves to, so there is no upgrade to perform.", alias="nothingToUpgrade")
    nothing_to_upgrade_summary: Optional[StrictStr] = Field(default=None, description="The message to show when nothingToUpgrade is true; empty otherwise.", alias="nothingToUpgradeSummary")
    readiness_score: Optional[StrictInt] = Field(default=None, description="The overall readiness score (0-100, higher is better); absent when the report did not assess readiness.", alias="readinessScore")
    recommendations: Optional[List[StrictStr]] = Field(default=None, description="Suggested actions to improve upgrade safety")
    report_summary: Optional[StrictStr] = Field(default=None, description="A human-readable summary of the readiness analysis", alias="reportSummary")
    resource_analysis: Optional[ResourceCapacityCheck] = Field(default=None, description="Contains resource capacity validation; absent when not evaluated.", alias="resourceAnalysis")
    risk_level: Optional[UpgradeRiskLevel] = Field(default=None, description="The assessed risk, Unknown when the report did not assess readiness.", alias="riskLevel")
    version_analysis: Optional[K8sVersionAnalysis] = Field(default=None, description="Contains Kubernetes version compatibility analysis; absent when not evaluated.", alias="versionAnalysis")
    warnings: Optional[List[ValidationIssue]] = Field(default=None, description="Non-blocking issues to be aware of")
    workload_analysis: Optional[WorkloadImpactAnalysis] = Field(default=None, description="Contains workload impact assessment; absent when not evaluated.", alias="workloadAnalysis")
    __properties: ClassVar[List[str]] = ["canProceed", "clusterHealth", "criticalIssues", "estimatedTime", "notEvaluated", "nothingToUpgrade", "nothingToUpgradeSummary", "readinessScore", "recommendations", "reportSummary", "resourceAnalysis", "riskLevel", "versionAnalysis", "warnings", "workloadAnalysis"]

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
        """Create an instance of UpgradeReadinessReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cluster_health
        if self.cluster_health:
            _dict['clusterHealth'] = self.cluster_health.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in critical_issues (list)
        _items = []
        if self.critical_issues:
            for _item_critical_issues in self.critical_issues:
                if _item_critical_issues:
                    _items.append(_item_critical_issues.to_dict())
            _dict['criticalIssues'] = _items
        # override the default output from pydantic by calling `to_dict()` of resource_analysis
        if self.resource_analysis:
            _dict['resourceAnalysis'] = self.resource_analysis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version_analysis
        if self.version_analysis:
            _dict['versionAnalysis'] = self.version_analysis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        # override the default output from pydantic by calling `to_dict()` of workload_analysis
        if self.workload_analysis:
            _dict['workloadAnalysis'] = self.workload_analysis.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpgradeReadinessReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canProceed": obj.get("canProceed"),
            "clusterHealth": ClusterHealthCheck.from_dict(obj["clusterHealth"]) if obj.get("clusterHealth") is not None else None,
            "criticalIssues": [ValidationIssue.from_dict(_item) for _item in obj["criticalIssues"]] if obj.get("criticalIssues") is not None else None,
            "estimatedTime": obj.get("estimatedTime"),
            "notEvaluated": obj.get("notEvaluated"),
            "nothingToUpgrade": obj.get("nothingToUpgrade"),
            "nothingToUpgradeSummary": obj.get("nothingToUpgradeSummary"),
            "readinessScore": obj.get("readinessScore"),
            "recommendations": obj.get("recommendations"),
            "reportSummary": obj.get("reportSummary"),
            "resourceAnalysis": ResourceCapacityCheck.from_dict(obj["resourceAnalysis"]) if obj.get("resourceAnalysis") is not None else None,
            "riskLevel": obj.get("riskLevel"),
            "versionAnalysis": K8sVersionAnalysis.from_dict(obj["versionAnalysis"]) if obj.get("versionAnalysis") is not None else None,
            "warnings": [ValidationIssue.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "workloadAnalysis": WorkloadImpactAnalysis.from_dict(obj["workloadAnalysis"]) if obj.get("workloadAnalysis") is not None else None
        })
        return _obj


