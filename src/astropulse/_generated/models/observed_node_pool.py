# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.observed_node_pool_change import ObservedNodePoolChange
from astropulse._generated.models.observed_node_pool_kind import ObservedNodePoolKind
from astropulse._generated.models.observed_node_set import ObservedNodeSet
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ObservedNodePool(BaseModel):
    """
    ObservedNodePool
    """ # noqa: E501
    change: Optional[ObservedNodePoolChange] = Field(default=None, description="Says what is happening to the pool's nodes right now, from what the cluster reports: nodes being reclaimed, removed or replaced, cordoned nodes, or more nodes than the group's maximum. Absent when nothing is.")
    kind: Optional[ObservedNodePoolKind] = Field(default=None, description="Why the pool's nodes exist.")
    label: Optional[StrictStr] = Field(default=None, description="Names the pool for a person: what its nodes are for and how they come and go, for example \"GPU pool (autoscaled)\" or \"Node group platform\".")
    name: Optional[StrictStr] = Field(default=None, description="The pool's name on the cluster: the node group's, or the autoscaling node pool's.")
    node_group: Optional[StrictStr] = Field(default=None, description="The name of the node group in workerNodes this pool is, when it is one of them.", alias="nodeGroup")
    sets: Optional[List[ObservedNodeSet]] = Field(default=None, description="Group the pool's nodes by machine type, capacity type and zone.")
    truncated: Optional[StrictBool] = Field(default=None, description="True when the pool has more sets than are listed.")
    __properties: ClassVar[List[str]] = ["change", "kind", "label", "name", "nodeGroup", "sets", "truncated"]

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
        """Create an instance of ObservedNodePool from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of change
        if self.change:
            _dict['change'] = self.change.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sets (list)
        _items = []
        if self.sets:
            for _item_sets in self.sets:
                if _item_sets:
                    _items.append(_item_sets.to_dict())
            _dict['sets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObservedNodePool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "change": ObservedNodePoolChange.from_dict(obj["change"]) if obj.get("change") is not None else None,
            "kind": obj.get("kind"),
            "label": obj.get("label"),
            "name": obj.get("name"),
            "nodeGroup": obj.get("nodeGroup"),
            "sets": [ObservedNodeSet.from_dict(_item) for _item in obj["sets"]] if obj.get("sets") is not None else None,
            "truncated": obj.get("truncated")
        })
        return _obj


