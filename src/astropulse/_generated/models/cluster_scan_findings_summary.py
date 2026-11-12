# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.scan_findings_no_result import ScanFindingsNoResult
from astropulse._generated.models.scan_findings_unscanned_images import ScanFindingsUnscannedImages
from astropulse._generated.models.workload_scan_finding import WorkloadScanFinding
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterScanFindingsSummary(BaseModel):
    """
    ClusterScanFindingsSummary
    """ # noqa: E501
    age_seconds: Optional[StrictInt] = Field(default=None, description="Computed at read time from ReportedAt: how long ago the scan completed.", alias="ageSeconds")
    cluster_name: Optional[StrictStr] = Field(default=None, alias="clusterName")
    no_result: Optional[List[ScanFindingsNoResult]] = Field(default=None, description="Lists every application and installed add-on on the cluster that has no scan result, with the reason for each.", alias="noResult")
    notes: Optional[List[StrictStr]] = Field(default=None, description="Plain sentences about what these results leave out, such as findings left out by platform policy. Absent when there is nothing to say.")
    received_at: Optional[StrictStr] = Field(default=None, description="When AstroPulse ingested this snapshot.", alias="receivedAt")
    reported_at: Optional[StrictStr] = Field(default=None, description="When the scan completed.", alias="reportedAt")
    unscanned_images: Optional[List[ScanFindingsUnscannedImages]] = Field(default=None, description="The images the scanner could not scan, grouped by reason. Absent when every scan left a result.", alias="unscannedImages")
    workloads: Optional[List[WorkloadScanFinding]] = None
    __properties: ClassVar[List[str]] = ["ageSeconds", "clusterName", "noResult", "notes", "receivedAt", "reportedAt", "unscannedImages", "workloads"]

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
        """Create an instance of ClusterScanFindingsSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in no_result (list)
        _items = []
        if self.no_result:
            for _item_no_result in self.no_result:
                if _item_no_result:
                    _items.append(_item_no_result.to_dict())
            _dict['noResult'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in unscanned_images (list)
        _items = []
        if self.unscanned_images:
            for _item_unscanned_images in self.unscanned_images:
                if _item_unscanned_images:
                    _items.append(_item_unscanned_images.to_dict())
            _dict['unscannedImages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in workloads (list)
        _items = []
        if self.workloads:
            for _item_workloads in self.workloads:
                if _item_workloads:
                    _items.append(_item_workloads.to_dict())
            _dict['workloads'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterScanFindingsSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ageSeconds": obj.get("ageSeconds"),
            "clusterName": obj.get("clusterName"),
            "noResult": [ScanFindingsNoResult.from_dict(_item) for _item in obj["noResult"]] if obj.get("noResult") is not None else None,
            "notes": obj.get("notes"),
            "receivedAt": obj.get("receivedAt"),
            "reportedAt": obj.get("reportedAt"),
            "unscannedImages": [ScanFindingsUnscannedImages.from_dict(_item) for _item in obj["unscannedImages"]] if obj.get("unscannedImages") is not None else None,
            "workloads": [WorkloadScanFinding.from_dict(_item) for _item in obj["workloads"]] if obj.get("workloads") is not None else None
        })
        return _obj


