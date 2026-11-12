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
from astropulse._generated.models.karpenter_consolidation_policy import KarpenterConsolidationPolicy
from astropulse._generated.models.karpenter_disruption_budget import KarpenterDisruptionBudget
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class KarpenterDisruption(BaseModel):
    """
    KarpenterDisruption
    """ # noqa: E501
    budgets: Optional[List[KarpenterDisruptionBudget]] = Field(default=None, description="Limits on how many nodes change at once; when several apply, the smallest wins. Left out, it is one budget of 10%.")
    consolidate_after: Optional[StrictStr] = Field(default=None, description="How long a node stays empty or underused before it is removed, from 30s (5m for GPU nodes) to 720h, or `Never`. Shorter saves idle cost; longer keeps the node ready for the next workload.", alias="consolidateAfter", json_schema_extra={"examples": ["5m"]})
    consolidation_policy: Optional[KarpenterConsolidationPolicy] = Field(default=None, description="Which nodes may be removed: only empty ones, or also underused ones, whose pods restart on fewer, cheaper nodes.", alias="consolidationPolicy")
    __properties: ClassVar[List[str]] = ["budgets", "consolidateAfter", "consolidationPolicy"]

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
        """Create an instance of KarpenterDisruption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in budgets (list)
        _items = []
        if self.budgets:
            for _item_budgets in self.budgets:
                if _item_budgets:
                    _items.append(_item_budgets.to_dict())
            _dict['budgets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KarpenterDisruption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "budgets": [KarpenterDisruptionBudget.from_dict(_item) for _item in obj["budgets"]] if obj.get("budgets") is not None else None,
            "consolidateAfter": obj.get("consolidateAfter"),
            "consolidationPolicy": obj.get("consolidationPolicy")
        })
        return _obj


