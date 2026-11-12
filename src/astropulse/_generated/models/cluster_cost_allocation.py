# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from astropulse._generated.models.cost_allocation_group_by import CostAllocationGroupBy
from astropulse._generated.models.cost_allocation_item import CostAllocationItem
from astropulse._generated.models.cost_allocation_sort_by import CostAllocationSortBy
from astropulse._generated.models.cost_window import CostWindow
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.sort_order import SortOrder
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterCostAllocation(BaseModel):
    """
    ClusterCostAllocation
    """ # noqa: E501
    allocations: Optional[List[CostAllocationItem]] = None
    cluster_id: Optional[StrictStr] = Field(default=None, alias="clusterId")
    cluster_name: Optional[StrictStr] = Field(default=None, alias="clusterName")
    complete: Optional[StrictBool] = None
    coverage_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="MeasuredWindows divided by ExpectedWindows.", alias="coveragePercent")
    currency: Optional[StrictStr] = None
    expected_windows: Optional[StrictInt] = Field(default=None, alias="expectedWindows")
    gap_windows: Optional[StrictInt] = Field(default=None, alias="gapWindows")
    group_by: Optional[CostAllocationGroupBy] = Field(default=None, description="What the allocations are broken down by.", alias="groupBy")
    has_more: Optional[StrictBool] = Field(default=None, alias="hasMore")
    measured_windows: Optional[StrictInt] = Field(default=None, description="Excludes both missing reports and explicit gaps.", alias="measuredWindows")
    missing_windows: Optional[StrictInt] = Field(default=None, alias="missingWindows")
    next_page_token: Optional[StrictStr] = Field(default=None, alias="nextPageToken")
    priced_from: Optional[StrictStr] = Field(default=None, description="The start of the first measured hour that carries a price. Absent when no hour is priced.", alias="pricedFrom")
    priced_windows: Optional[StrictInt] = Field(default=None, description="The number of measured hours that carry a price.", alias="pricedWindows")
    pricing_notes: Optional[List[Notice]] = Field(default=None, description="Say how the cluster's cost is priced where its figures are not what they seem.", alias="pricingNotes")
    reported_windows: Optional[StrictInt] = Field(default=None, alias="reportedWindows")
    returned_items: Optional[StrictInt] = Field(default=None, alias="returnedItems")
    sort_by: Optional[CostAllocationSortBy] = Field(default=None, description="What the allocations are ordered by.", alias="sortBy")
    sort_order: Optional[SortOrder] = Field(default=None, description="The direction of the order.", alias="sortOrder")
    total_items: Optional[StrictInt] = Field(default=None, alias="totalItems")
    unattributed: Optional[List[CostAllocationItem]] = Field(default=None, description="Spend that belongs to no row of the breakdown, such as idle capacity, cluster management and NAT gateways, each with its `kind`. It is the same on every page, and with the allocations of every page of an unfiltered breakdown it adds up to the cluster total.")
    unpriced_windows: Optional[StrictInt] = Field(default=None, description="The number of measured hours with no price: their usage is in the dimensions and not in the costs.", alias="unpricedWindows")
    window: Optional[CostWindow] = None
    __properties: ClassVar[List[str]] = ["allocations", "clusterId", "clusterName", "complete", "coveragePercent", "currency", "expectedWindows", "gapWindows", "groupBy", "hasMore", "measuredWindows", "missingWindows", "nextPageToken", "pricedFrom", "pricedWindows", "pricingNotes", "reportedWindows", "returnedItems", "sortBy", "sortOrder", "totalItems", "unattributed", "unpricedWindows", "window"]

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
        """Create an instance of ClusterCostAllocation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_notes (list)
        _items = []
        if self.pricing_notes:
            for _item_pricing_notes in self.pricing_notes:
                if _item_pricing_notes:
                    _items.append(_item_pricing_notes.to_dict())
            _dict['pricingNotes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in unattributed (list)
        _items = []
        if self.unattributed:
            for _item_unattributed in self.unattributed:
                if _item_unattributed:
                    _items.append(_item_unattributed.to_dict())
            _dict['unattributed'] = _items
        # override the default output from pydantic by calling `to_dict()` of window
        if self.window:
            _dict['window'] = self.window.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterCostAllocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allocations": [CostAllocationItem.from_dict(_item) for _item in obj["allocations"]] if obj.get("allocations") is not None else None,
            "clusterId": obj.get("clusterId"),
            "clusterName": obj.get("clusterName"),
            "complete": obj.get("complete"),
            "coveragePercent": obj.get("coveragePercent"),
            "currency": obj.get("currency"),
            "expectedWindows": obj.get("expectedWindows"),
            "gapWindows": obj.get("gapWindows"),
            "groupBy": obj.get("groupBy"),
            "hasMore": obj.get("hasMore"),
            "measuredWindows": obj.get("measuredWindows"),
            "missingWindows": obj.get("missingWindows"),
            "nextPageToken": obj.get("nextPageToken"),
            "pricedFrom": obj.get("pricedFrom"),
            "pricedWindows": obj.get("pricedWindows"),
            "pricingNotes": [Notice.from_dict(_item) for _item in obj["pricingNotes"]] if obj.get("pricingNotes") is not None else None,
            "reportedWindows": obj.get("reportedWindows"),
            "returnedItems": obj.get("returnedItems"),
            "sortBy": obj.get("sortBy"),
            "sortOrder": obj.get("sortOrder"),
            "totalItems": obj.get("totalItems"),
            "unattributed": [CostAllocationItem.from_dict(_item) for _item in obj["unattributed"]] if obj.get("unattributed") is not None else None,
            "unpricedWindows": obj.get("unpricedWindows"),
            "window": CostWindow.from_dict(obj["window"]) if obj.get("window") is not None else None
        })
        return _obj


