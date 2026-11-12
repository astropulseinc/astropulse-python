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
from astropulse._generated.models.agent_capability_state import AgentCapabilityState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AgentCapabilityStatus(BaseModel):
    """
    AgentCapabilityStatus
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, description="The capability's name as people read it (e.g. \"cost reporting\").", alias="displayName")
    idle: Optional[StrictBool] = Field(default=None, description="True when the capability is ready and has nothing on the cluster to check yet; the message says what is missing.")
    message: Optional[StrictStr] = Field(default=None, description="One complete sentence saying what the state means for this capability on this cluster.")
    name: Optional[StrictStr] = Field(default=None, description="The capability's identifier (e.g. \"health-v1\").")
    state: Optional[AgentCapabilityState] = Field(default=None, description="The capability's state. A capability that is running and has no data to report yet is reported as Starting, with `waiting` set.")
    waiting: Optional[StrictBool] = Field(default=None, description="True when the capability is running and is waiting for its first data. Nothing is wrong with it; the message says what it waits for.")
    __properties: ClassVar[List[str]] = ["displayName", "idle", "message", "name", "state", "waiting"]

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
        """Create an instance of AgentCapabilityStatus from a JSON string"""
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
        """Create an instance of AgentCapabilityStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "displayName": obj.get("displayName"),
            "idle": obj.get("idle"),
            "message": obj.get("message"),
            "name": obj.get("name"),
            "state": obj.get("state"),
            "waiting": obj.get("waiting")
        })
        return _obj


