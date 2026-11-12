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
from astropulse._generated.models.instance_type import InstanceType
from astropulse._generated.models.node_group_change_type import NodeGroupChangeType
from astropulse._generated.models.node_group_update_strategy import NodeGroupUpdateStrategy
from astropulse._generated.models.upgrade_plan_node_pool_state import UpgradePlanNodePoolState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpgradePlanNodePool(BaseModel):
    """
    UpgradePlanNodePool
    """ # noqa: E501
    change_type: Optional[NodeGroupChangeType] = Field(default=None, description="Describes what is changing for this node pool.", alias="changeType")
    current: Optional[UpgradePlanNodePoolState] = Field(default=None, description="The node pool as it is before the update; absent for a node pool the update creates.")
    instance_type: Optional[InstanceType] = Field(default=None, description="How the node pool's nodes are bought once the update is applied.", alias="instanceType")
    machine_types: Optional[List[StrictStr]] = Field(default=None, description="Lists the instance types in this node pool once the update is applied.", alias="machineTypes")
    max_nodes: Optional[StrictInt] = Field(default=None, description="The maximum node count once the update is applied.", alias="maxNodes")
    min_nodes: Optional[StrictInt] = Field(default=None, description="The minimum node count once the update is applied.", alias="minNodes")
    name: Optional[StrictStr] = Field(default=None, description="The node pool name")
    strategy: Optional[NodeGroupUpdateStrategy] = Field(default=None, description="Describes how this specific node pool will be updated.")
    __properties: ClassVar[List[str]] = ["changeType", "current", "instanceType", "machineTypes", "maxNodes", "minNodes", "name", "strategy"]

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
        """Create an instance of UpgradePlanNodePool from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of current
        if self.current:
            _dict['current'] = self.current.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpgradePlanNodePool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "changeType": obj.get("changeType"),
            "current": UpgradePlanNodePoolState.from_dict(obj["current"]) if obj.get("current") is not None else None,
            "instanceType": obj.get("instanceType"),
            "machineTypes": obj.get("machineTypes"),
            "maxNodes": obj.get("maxNodes"),
            "minNodes": obj.get("minNodes"),
            "name": obj.get("name"),
            "strategy": obj.get("strategy")
        })
        return _obj


