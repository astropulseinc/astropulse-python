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
from astropulse._generated.models.application_metrics_allocation_item import ApplicationMetricsAllocationItem
from astropulse._generated.models.cluster_metrics_sort_field import ClusterMetricsSortField
from astropulse._generated.models.cost_window import CostWindow
from astropulse._generated.models.sort_order import SortOrder
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterMetricsAllocation(BaseModel):
    """
    ClusterMetricsAllocation
    """ # noqa: E501
    allocations: Optional[List[ApplicationMetricsAllocationItem]] = Field(default=None, description="Page-limited by the request's limit/offset. Unlike ClusterCostAllocation's opaque, window-pinning NextPageToken, paging here is plain offset+limit: a metrics read is a live re-query of a small ephemeral store, not an accounting read over an immutable billing window, so there is nothing to pin and reissuing the read for the next page is always current.")
    cluster_id: Optional[StrictStr] = Field(default=None, description="Identifies the cluster.", alias="clusterId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="Its name.", alias="clusterName")
    empty_message: Optional[StrictStr] = Field(default=None, description="Says why no application is listed and what to do next. Set only when none reported usage in the window, or none matched the search.", alias="emptyMessage")
    has_more: Optional[StrictBool] = Field(default=None, description="Reports whether another page follows.", alias="hasMore")
    returned_items: Optional[StrictInt] = Field(default=None, description="How many of them this page carries.", alias="returnedItems")
    sort_by: Optional[ClusterMetricsSortField] = Field(default=None, description="The dimension the page is ordered on.", alias="sortBy")
    sort_order: Optional[SortOrder] = Field(default=None, description="The direction the page is ordered in.", alias="sortOrder")
    total_items: Optional[StrictInt] = Field(default=None, description="How many applications reported in the window.", alias="totalItems")
    window: Optional[CostWindow] = Field(default=None, description="The time range these readings cover.")
    __properties: ClassVar[List[str]] = ["allocations", "clusterId", "clusterName", "emptyMessage", "hasMore", "returnedItems", "sortBy", "sortOrder", "totalItems", "window"]

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
        """Create an instance of ClusterMetricsAllocation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in allocations (list)
        _items = []
        if self.allocations:
            for _item_allocations in self.allocations:
                if _item_allocations:
                    _items.append(_item_allocations.to_dict())
            _dict['allocations'] = _items
        # override the default output from pydantic by calling `to_dict()` of window
        if self.window:
            _dict['window'] = self.window.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterMetricsAllocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allocations": [ApplicationMetricsAllocationItem.from_dict(_item) for _item in obj["allocations"]] if obj.get("allocations") is not None else None,
            "clusterId": obj.get("clusterId"),
            "clusterName": obj.get("clusterName"),
            "emptyMessage": obj.get("emptyMessage"),
            "hasMore": obj.get("hasMore"),
            "returnedItems": obj.get("returnedItems"),
            "sortBy": obj.get("sortBy"),
            "sortOrder": obj.get("sortOrder"),
            "totalItems": obj.get("totalItems"),
            "window": CostWindow.from_dict(obj["window"]) if obj.get("window") is not None else None
        })
        return _obj


