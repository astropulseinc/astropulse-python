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
from astropulse._generated.models.accelerator_metrics_summary import AcceleratorMetricsSummary
from astropulse._generated.models.cost_window import CostWindow
from astropulse._generated.models.inference_metrics_summary import InferenceMetricsSummary
from astropulse._generated.models.metrics_series_point import MetricsSeriesPoint
from astropulse._generated.models.queue_metrics_summary import QueueMetricsSummary
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationMetricsSeries(BaseModel):
    """
    ApplicationMetricsSeries
    """ # noqa: E501
    accelerator_summary: Optional[AcceleratorMetricsSummary] = Field(default=None, description="What the application's accelerators did across the whole window, present only for an application holding a device. Use it for the range's figures: a point describes its own window.", alias="acceleratorSummary")
    application_name: Optional[StrictStr] = Field(default=None, description="The application's own name.", alias="applicationName")
    cluster_id: Optional[StrictStr] = Field(default=None, description="Identifies that cluster.", alias="clusterId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster the application runs on.", alias="clusterName")
    generated_app_name: Optional[StrictStr] = Field(default=None, description="The name AstroPulse gave the workload in-cluster.", alias="generatedAppName")
    inference_summary: Optional[InferenceMetricsSummary] = Field(default=None, description="The model's behaviour across the whole window, present only for an application that serves one. Use it for \"the p99 over this range\": the per-point percentiles describe their own windows and must never be averaged together.", alias="inferenceSummary")
    points: Optional[List[MetricsSeriesPoint]] = Field(default=None, description="The samples in the window, oldest first. A window with no stored sample is absent rather than reported as zero.")
    queue_summary: Optional[QueueMetricsSummary] = Field(default=None, description="The application's life in its workload queue across the whole window, present only for an application whose pods name a queue.", alias="queueSummary")
    window: Optional[CostWindow] = Field(default=None, description="The time range these points cover.")
    __properties: ClassVar[List[str]] = ["acceleratorSummary", "applicationName", "clusterId", "clusterName", "generatedAppName", "inferenceSummary", "points", "queueSummary", "window"]

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
        """Create an instance of ApplicationMetricsSeries from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accelerator_summary
        if self.accelerator_summary:
            _dict['acceleratorSummary'] = self.accelerator_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inference_summary
        if self.inference_summary:
            _dict['inferenceSummary'] = self.inference_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in points (list)
        _items = []
        if self.points:
            for _item_points in self.points:
                if _item_points:
                    _items.append(_item_points.to_dict())
            _dict['points'] = _items
        # override the default output from pydantic by calling `to_dict()` of queue_summary
        if self.queue_summary:
            _dict['queueSummary'] = self.queue_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of window
        if self.window:
            _dict['window'] = self.window.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationMetricsSeries from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "acceleratorSummary": AcceleratorMetricsSummary.from_dict(obj["acceleratorSummary"]) if obj.get("acceleratorSummary") is not None else None,
            "applicationName": obj.get("applicationName"),
            "clusterId": obj.get("clusterId"),
            "clusterName": obj.get("clusterName"),
            "generatedAppName": obj.get("generatedAppName"),
            "inferenceSummary": InferenceMetricsSummary.from_dict(obj["inferenceSummary"]) if obj.get("inferenceSummary") is not None else None,
            "points": [MetricsSeriesPoint.from_dict(_item) for _item in obj["points"]] if obj.get("points") is not None else None,
            "queueSummary": QueueMetricsSummary.from_dict(obj["queueSummary"]) if obj.get("queueSummary") is not None else None,
            "window": CostWindow.from_dict(obj["window"]) if obj.get("window") is not None else None
        })
        return _obj


