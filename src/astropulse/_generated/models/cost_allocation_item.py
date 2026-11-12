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
from astropulse._generated.models.cost_dimensions import CostDimensions
from astropulse._generated.models.cost_group import CostGroup
from astropulse._generated.models.cost_row_kind import CostRowKind
from astropulse._generated.models.cost_total import CostTotal
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CostAllocationItem(BaseModel):
    """
    CostAllocationItem
    """ # noqa: E501
    costs: Optional[List[CostTotal]] = None
    dimensions: Optional[CostDimensions] = None
    group: Optional[CostGroup] = Field(default=None, description="The group the row is shown under, from its kind.")
    kind: Optional[CostRowKind] = Field(default=None, description="What the row is.")
    name: Optional[StrictStr] = Field(default=None, description="The namespace, application or node group the row is for. A row of a fixed kind is named by its code: its `kind`, such as `Idle`, or for a `ClusterInfrastructure` row its ClusterInfrastructureItem, such as `NATGateway`.")
    __properties: ClassVar[List[str]] = ["costs", "dimensions", "group", "kind", "name"]

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
        """Create an instance of CostAllocationItem from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CostAllocationItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "costs": [CostTotal.from_dict(_item) for _item in obj["costs"]] if obj.get("costs") is not None else None,
            "dimensions": CostDimensions.from_dict(obj["dimensions"]) if obj.get("dimensions") is not None else None,
            "group": obj.get("group"),
            "kind": obj.get("kind"),
            "name": obj.get("name")
        })
        return _obj


