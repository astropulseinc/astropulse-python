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
from astropulse._generated.models.timeline_event_kind import TimelineEventKind
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TimelineEvent(BaseModel):
    """
    TimelineEvent
    """ # noqa: E501
    actor: Optional[StrictStr] = Field(default=None, description="Who triggered a deploy/rollback event.")
    actor_display: Optional[StrictStr] = Field(default=None, description="The human-readable actor (name, falling back to email) resolved from Actor. Best-effort; empty when unresolved. Org-scoped, so no cross-org identity leak.", alias="actorDisplay")
    at: Optional[StrictStr] = Field(default=None, description="The RFC3339 event timestamp.")
    health: Optional[StrictStr] = Field(default=None, description="The live health for drift events.")
    kind: Optional[TimelineEventKind] = Field(default=None, description="The event kind.")
    summary: Optional[StrictStr] = Field(default=None, description="A short human-readable description.")
    sync: Optional[StrictStr] = Field(default=None, description="The live sync status for drift events.")
    version: Optional[StrictStr] = Field(default=None, description="The Astro version for deploy/rollback events.")
    __properties: ClassVar[List[str]] = ["actor", "actorDisplay", "at", "health", "kind", "summary", "sync", "version"]

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
        """Create an instance of TimelineEvent from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimelineEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actor": obj.get("actor"),
            "actorDisplay": obj.get("actorDisplay"),
            "at": obj.get("at"),
            "health": obj.get("health"),
            "kind": obj.get("kind"),
            "summary": obj.get("summary"),
            "sync": obj.get("sync"),
            "version": obj.get("version")
        })
        return _obj


