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
from astropulse._generated.models.node_group_update_strategy import NodeGroupUpdateStrategy
from astropulse._generated.models.upgrade_plan_node_pool import UpgradePlanNodePool
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpgradePlanPhase(BaseModel):
    """
    UpgradePlanPhase
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Explains what happens during this phase")
    details: Optional[List[StrictStr]] = Field(default=None, description="Provides additional context about this phase")
    estimated_duration: Optional[StrictStr] = Field(default=None, description="The expected time for this phase (e.g. \"5m\", \"15m\")", alias="estimatedDuration")
    name: Optional[StrictStr] = Field(default=None, description="The phase identifier (e.g. \"Control Plane Upgrade\", \"Node Pool Rolling Update\")")
    node_pools: Optional[List[UpgradePlanNodePool]] = Field(default=None, description="Lists the node pools affected by this phase", alias="nodePools")
    strategy: Optional[NodeGroupUpdateStrategy] = Field(default=None, description="Describes how this phase will be executed. Automatically selected based on what is changing and the provider's capabilities.")
    __properties: ClassVar[List[str]] = ["description", "details", "estimatedDuration", "name", "nodePools", "strategy"]

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
        """Create an instance of UpgradePlanPhase from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in node_pools (list)
        _items = []
        if self.node_pools:
            for _item_node_pools in self.node_pools:
                if _item_node_pools:
                    _items.append(_item_node_pools.to_dict())
            _dict['nodePools'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpgradePlanPhase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "details": obj.get("details"),
            "estimatedDuration": obj.get("estimatedDuration"),
            "name": obj.get("name"),
            "nodePools": [UpgradePlanNodePool.from_dict(_item) for _item in obj["nodePools"]] if obj.get("nodePools") is not None else None,
            "strategy": obj.get("strategy")
        })
        return _obj


