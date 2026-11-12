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
from astropulse._generated.models.cost_dimensions import CostDimensions
from astropulse._generated.models.cost_total import CostTotal
from astropulse._generated.models.cost_window import CostWindow
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonCostSummary(BaseModel):
    """
    ClusterAddonCostSummary
    """ # noqa: E501
    application_name: Optional[StrictStr] = Field(default=None, alias="applicationName")
    cluster_name: Optional[StrictStr] = Field(default=None, alias="clusterName")
    complete: Optional[StrictBool] = None
    costs: Optional[List[CostTotal]] = None
    coverage_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="coveragePercent")
    dimensions: Optional[CostDimensions] = None
    expected_windows: Optional[StrictInt] = Field(default=None, alias="expectedWindows")
    gap_windows: Optional[StrictInt] = Field(default=None, alias="gapWindows")
    measured_windows: Optional[StrictInt] = Field(default=None, alias="measuredWindows")
    missing_windows: Optional[StrictInt] = Field(default=None, alias="missingWindows")
    priced_from: Optional[StrictStr] = Field(default=None, description="The start of the first measured hour that carries a price. Absent when no hour is priced.", alias="pricedFrom")
    priced_windows: Optional[StrictInt] = Field(default=None, description="The number of measured hours that carry a price.", alias="pricedWindows")
    pricing_notes: Optional[List[Notice]] = Field(default=None, description="Say how the cluster's cost is priced where its figures are not what they seem.", alias="pricingNotes")
    reported_windows: Optional[StrictInt] = Field(default=None, alias="reportedWindows")
    reporting: Optional[StrictBool] = None
    unpriced_windows: Optional[StrictInt] = Field(default=None, description="The number of measured hours with no price: their usage is in the dimensions and not in the costs.", alias="unpricedWindows")
    window: Optional[CostWindow] = None
    __properties: ClassVar[List[str]] = ["applicationName", "clusterName", "complete", "costs", "coveragePercent", "dimensions", "expectedWindows", "gapWindows", "measuredWindows", "missingWindows", "pricedFrom", "pricedWindows", "pricingNotes", "reportedWindows", "reporting", "unpricedWindows", "window"]

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
        """Create an instance of ClusterAddonCostSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in costs (list)
        _items = []
        if self.costs:
            for _item_costs in self.costs:
                if _item_costs:
                    _items.append(_item_costs.to_dict())
            _dict['costs'] = _items
        # override the default output from pydantic by calling `to_dict()` of dimensions
        if self.dimensions:
            _dict['dimensions'] = self.dimensions.to_dict()
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
        """Create an instance of ClusterAddonCostSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationName": obj.get("applicationName"),
            "clusterName": obj.get("clusterName"),
            "complete": obj.get("complete"),
            "costs": [CostTotal.from_dict(_item) for _item in obj["costs"]] if obj.get("costs") is not None else None,
            "coveragePercent": obj.get("coveragePercent"),
            "dimensions": CostDimensions.from_dict(obj["dimensions"]) if obj.get("dimensions") is not None else None,
            "expectedWindows": obj.get("expectedWindows"),
            "gapWindows": obj.get("gapWindows"),
            "measuredWindows": obj.get("measuredWindows"),
            "missingWindows": obj.get("missingWindows"),
            "pricedFrom": obj.get("pricedFrom"),
            "pricedWindows": obj.get("pricedWindows"),
            "pricingNotes": [Notice.from_dict(_item) for _item in obj["pricingNotes"]] if obj.get("pricingNotes") is not None else None,
            "reportedWindows": obj.get("reportedWindows"),
            "reporting": obj.get("reporting"),
            "unpricedWindows": obj.get("unpricedWindows"),
            "window": CostWindow.from_dict(obj["window"]) if obj.get("window") is not None else None
        })
        return _obj


