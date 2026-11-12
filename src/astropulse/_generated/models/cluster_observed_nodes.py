# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.observed_node_pool import ObservedNodePool
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterObservedNodes(BaseModel):
    """
    ClusterObservedNodes
    """ # noqa: E501
    observed_at: Optional[datetime] = Field(default=None, description="When the agent last reported, in RFC 3339. While the cluster is Disconnected it is the last report before that, and the pools may be out of date.", alias="observedAt")
    pools: Optional[List[ObservedNodePool]] = Field(default=None, description="The cluster's node pools: its node groups and the pools an autoscaler launches nodes into. Empty when the agent reported no nodes.")
    truncated: Optional[StrictBool] = Field(default=None, description="True when the cluster has more pools than are listed.")
    __properties: ClassVar[List[str]] = ["observedAt", "pools", "truncated"]

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
        """Create an instance of ClusterObservedNodes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in pools (list)
        _items = []
        if self.pools:
            for _item_pools in self.pools:
                if _item_pools:
                    _items.append(_item_pools.to_dict())
            _dict['pools'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterObservedNodes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "observedAt": obj.get("observedAt"),
            "pools": [ObservedNodePool.from_dict(_item) for _item in obj["pools"]] if obj.get("pools") is not None else None,
            "truncated": obj.get("truncated")
        })
        return _obj


