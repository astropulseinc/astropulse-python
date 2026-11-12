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
from astropulse._generated.models.user_event_count import UserEventCount
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AuditStats(BaseModel):
    """
    AuditStats
    """ # noqa: E501
    events_by_action: Optional[Dict[str, StrictInt]] = Field(default=None, description="Counts events per action, keyed by the action, such as Create.", alias="eventsByAction")
    events_by_type: Optional[Dict[str, StrictInt]] = Field(default=None, description="Counts events per event type, keyed by the event type, such as Cluster.", alias="eventsByType")
    org_id: Optional[StrictStr] = Field(default=None, description="The organization these statistics are for", alias="orgId")
    period: Optional[StrictStr] = Field(default=None, description="Indicates the time period for these statistics (7d, 30d, 90d)")
    top_users: Optional[List[UserEventCount]] = Field(default=None, description="Lists the users with the most audit events", alias="topUsers")
    total_events: Optional[StrictInt] = Field(default=None, description="The total number of audit events in the specified period", alias="totalEvents")
    __properties: ClassVar[List[str]] = ["eventsByAction", "eventsByType", "orgId", "period", "topUsers", "totalEvents"]

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
        """Create an instance of AuditStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in top_users (list)
        _items = []
        if self.top_users:
            for _item_top_users in self.top_users:
                if _item_top_users:
                    _items.append(_item_top_users.to_dict())
            _dict['topUsers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventsByAction": obj.get("eventsByAction"),
            "eventsByType": obj.get("eventsByType"),
            "orgId": obj.get("orgId"),
            "period": obj.get("period"),
            "topUsers": [UserEventCount.from_dict(_item) for _item in obj["topUsers"]] if obj.get("topUsers") is not None else None,
            "totalEvents": obj.get("totalEvents")
        })
        return _obj


