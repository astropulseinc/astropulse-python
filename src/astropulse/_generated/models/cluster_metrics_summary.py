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
from astropulse._generated.models.cost_window import CostWindow
from astropulse._generated.models.metrics_dimensions import MetricsDimensions
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterMetricsSummary(BaseModel):
    """
    ClusterMetricsSummary
    """ # noqa: E501
    application_count: Optional[StrictInt] = Field(default=None, description="Every platform-managed application deployed to the cluster, regardless of whether it reported in this window.", alias="applicationCount")
    cluster_id: Optional[StrictStr] = Field(default=None, description="Identifies the cluster.", alias="clusterId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="Its name.", alias="clusterName")
    complete: Optional[StrictBool] = Field(default=None, description="False if any one reporting application had a sample with partial coverage — the collector could not reach every workload instance it expected. True when there were zero incomplete samples, including when there were zero samples at all.")
    empty_message: Optional[StrictStr] = Field(default=None, description="Says why no application reported usage in the window and what to do next. Set only when none did.", alias="emptyMessage")
    last_received_at: Optional[StrictStr] = Field(default=None, description="The most recent sample window-end across every reporting application, absent when nothing reported.", alias="lastReceivedAt")
    reporting_application_count: Optional[StrictInt] = Field(default=None, description="The subset of ApplicationCount that had at least one stored sample in the window. The gap between the two counts is exactly how many applications reported nothing — never inferred from a zero reading.", alias="reportingApplicationCount")
    sample_count: Optional[StrictInt] = Field(default=None, description="The total stored samples every reporting application contributed in the window.", alias="sampleCount")
    totals: Optional[MetricsDimensions] = Field(default=None, description="What every reporting application added up to.")
    window: Optional[CostWindow] = Field(default=None, description="The time range this summary covers.")
    __properties: ClassVar[List[str]] = ["applicationCount", "clusterId", "clusterName", "complete", "emptyMessage", "lastReceivedAt", "reportingApplicationCount", "sampleCount", "totals", "window"]

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
        """Create an instance of ClusterMetricsSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of totals
        if self.totals:
            _dict['totals'] = self.totals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of window
        if self.window:
            _dict['window'] = self.window.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterMetricsSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationCount": obj.get("applicationCount"),
            "clusterId": obj.get("clusterId"),
            "clusterName": obj.get("clusterName"),
            "complete": obj.get("complete"),
            "emptyMessage": obj.get("emptyMessage"),
            "lastReceivedAt": obj.get("lastReceivedAt"),
            "reportingApplicationCount": obj.get("reportingApplicationCount"),
            "sampleCount": obj.get("sampleCount"),
            "totals": MetricsDimensions.from_dict(obj["totals"]) if obj.get("totals") is not None else None,
            "window": CostWindow.from_dict(obj["window"]) if obj.get("window") is not None else None
        })
        return _obj


