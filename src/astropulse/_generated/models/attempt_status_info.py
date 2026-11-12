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
from astropulse._generated.models.attempt_status import AttemptStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AttemptStatusInfo(BaseModel):
    """
    AttemptStatusInfo
    """ # noqa: E501
    completed_at: Optional[StrictStr] = Field(default=None, description="The timestamp when the attempt completed (RFC 3339 format)", alias="completedAt")
    reason: Optional[StrictStr] = Field(default=None, description="Provides details about the current status or failure cause")
    started_at: Optional[StrictStr] = Field(default=None, description="The timestamp when the attempt started (RFC 3339 format)", alias="startedAt")
    status: Optional[AttemptStatus] = Field(default=None, description="The outcome of the attempt.")
    suggested_action: Optional[StrictStr] = Field(default=None, description="A recommended next step when the attempt fails", alias="suggestedAction")
    __properties: ClassVar[List[str]] = ["completedAt", "reason", "startedAt", "status", "suggestedAction"]

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
        """Create an instance of AttemptStatusInfo from a JSON string"""
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
        """Create an instance of AttemptStatusInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completedAt": obj.get("completedAt"),
            "reason": obj.get("reason"),
            "startedAt": obj.get("startedAt"),
            "status": obj.get("status"),
            "suggestedAction": obj.get("suggestedAction")
        })
        return _obj


