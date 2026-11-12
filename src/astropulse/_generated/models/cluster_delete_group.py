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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_delete_group_kind import ClusterDeleteGroupKind
from astropulse._generated.models.cluster_delete_item import ClusterDeleteItem
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterDeleteGroup(BaseModel):
    """
    ClusterDeleteGroup
    """ # noqa: E501
    attention: Optional[StrictBool] = Field(default=None, description="True when the group has items kept or needing your action.")
    confirmed: Optional[StrictBool] = Field(default=None, description="True when the items are what the delete did, false when they are what it would do.")
    items: Optional[List[ClusterDeleteItem]] = Field(default=None, description="The group's items, those kept or needing action first; it may be capped, with the rest named by moreSummary.")
    kind: Optional[ClusterDeleteGroupKind] = Field(default=None, description="The group's kind.")
    listed: Optional[StrictBool] = Field(default=None, description="False when the group's items could not be listed; it never means there are none.")
    listed_at: Optional[datetime] = Field(default=None, description="When the group's items were listed.", alias="listedAt")
    more_summary: Optional[StrictStr] = Field(default=None, description="Names the items past the cap, such as \"and 450 more\", when the list is capped.", alias="moreSummary")
    stale: Optional[StrictBool] = Field(default=None, description="True when that list is older than it should be, so an item may have changed since.")
    summary: Optional[StrictStr] = Field(default=None, description="One line for the group, such as \"34 removed, 3 kept\".")
    title: Optional[StrictStr] = Field(default=None, description="Names the group, such as \"Volumes\".")
    total: Optional[StrictInt] = Field(default=None, description="How many items the group has, including any not in items.")
    __properties: ClassVar[List[str]] = ["attention", "confirmed", "items", "kind", "listed", "listedAt", "moreSummary", "stale", "summary", "title", "total"]

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
        """Create an instance of ClusterDeleteGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterDeleteGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attention": obj.get("attention"),
            "confirmed": obj.get("confirmed"),
            "items": [ClusterDeleteItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "kind": obj.get("kind"),
            "listed": obj.get("listed"),
            "listedAt": obj.get("listedAt"),
            "moreSummary": obj.get("moreSummary"),
            "stale": obj.get("stale"),
            "summary": obj.get("summary"),
            "title": obj.get("title"),
            "total": obj.get("total")
        })
        return _obj


