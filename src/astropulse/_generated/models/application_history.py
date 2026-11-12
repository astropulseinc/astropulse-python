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
from astropulse._generated.models.application_rollback_state import ApplicationRollbackState
from astropulse._generated.models.application_version_entry import ApplicationVersionEntry
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.timeline_event import TimelineEvent
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationHistory(BaseModel):
    """
    ApplicationHistory
    """ # noqa: E501
    application_name: Optional[StrictStr] = Field(default=None, description="The user-facing application name.", alias="applicationName")
    current_version: Optional[StrictStr] = Field(default=None, description="The Astro version currently deployed.", alias="currentVersion")
    entries: Optional[List[ApplicationVersionEntry]] = Field(default=None, description="The deploy history, newest first.")
    notices: Optional[List[Notice]] = Field(default=None, description="Say what this history could not confirm, such as which versions can still be rolled back to; absent when there is nothing to say.")
    rollback_state: Optional[ApplicationRollbackState] = Field(default=None, description="The current Astro rollback/pin state.", alias="rollbackState")
    timeline: Optional[List[TimelineEvent]] = Field(default=None, description="Merges deploys/rollbacks and live-state drift events, newest first.")
    __properties: ClassVar[List[str]] = ["applicationName", "currentVersion", "entries", "notices", "rollbackState", "timeline"]

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
        """Create an instance of ApplicationHistory from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entries (list)
        _items = []
        if self.entries:
            for _item_entries in self.entries:
                if _item_entries:
                    _items.append(_item_entries.to_dict())
            _dict['entries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in timeline (list)
        _items = []
        if self.timeline:
            for _item_timeline in self.timeline:
                if _item_timeline:
                    _items.append(_item_timeline.to_dict())
            _dict['timeline'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationName": obj.get("applicationName"),
            "currentVersion": obj.get("currentVersion"),
            "entries": [ApplicationVersionEntry.from_dict(_item) for _item in obj["entries"]] if obj.get("entries") is not None else None,
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "rollbackState": obj.get("rollbackState"),
            "timeline": [TimelineEvent.from_dict(_item) for _item in obj["timeline"]] if obj.get("timeline") is not None else None
        })
        return _obj


