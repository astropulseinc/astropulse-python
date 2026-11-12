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
from astropulse._generated.models.cost_allocation_group_by import CostAllocationGroupBy
from astropulse._generated.models.cost_series_point import CostSeriesPoint
from astropulse._generated.models.cost_window import CostWindow
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterCostSeries(BaseModel):
    """
    ClusterCostSeries
    """ # noqa: E501
    cluster_id: Optional[StrictStr] = Field(default=None, alias="clusterId")
    cluster_name: Optional[StrictStr] = Field(default=None, alias="clusterName")
    group_by: Optional[CostAllocationGroupBy] = Field(default=None, description="The breakdown `name` is a row of; absent for the whole cluster.", alias="groupBy")
    interval: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    points: Optional[List[CostSeriesPoint]] = None
    pricing_notes: Optional[List[Notice]] = Field(default=None, description="Say how the cluster's cost is priced where its figures are not what they seem.", alias="pricingNotes")
    window: Optional[CostWindow] = None
    __properties: ClassVar[List[str]] = ["clusterId", "clusterName", "groupBy", "interval", "name", "points", "pricingNotes", "window"]

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
        """Create an instance of ClusterCostSeries from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in points (list)
        _items = []
        if self.points:
            for _item_points in self.points:
                if _item_points:
                    _items.append(_item_points.to_dict())
            _dict['points'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_notes (list)
        _items = []
        if self.pricing_notes:
            for _item_pricing_notes in self.pricing_notes:
                if _item_pricing_notes:
                    _items.append(_item_pricing_notes.to_dict())
            _dict['pricingNotes'] = _items
        # override the default output from pydantic by calling `to_dict()` of window
        if self.window:
            _dict['window'] = self.window.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterCostSeries from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "clusterName": obj.get("clusterName"),
            "groupBy": obj.get("groupBy"),
            "interval": obj.get("interval"),
            "name": obj.get("name"),
            "points": [CostSeriesPoint.from_dict(_item) for _item in obj["points"]] if obj.get("points") is not None else None,
            "pricingNotes": [Notice.from_dict(_item) for _item in obj["pricingNotes"]] if obj.get("pricingNotes") is not None else None,
            "window": CostWindow.from_dict(obj["window"]) if obj.get("window") is not None else None
        })
        return _obj


