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
from astropulse._generated.models.next_step import NextStep
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonHealthCheck(BaseModel):
    """
    ClusterAddonHealthCheck
    """ # noqa: E501
    idle: Optional[StrictBool] = Field(default=None, description="True when the check passes because there is nothing for it to check yet. An idle check always has a message saying what is missing.")
    message: Optional[StrictStr] = Field(default=None, description="Says what was found, when passing alone does not explain it.")
    name: Optional[StrictStr] = Field(default=None, description="What was checked.")
    next_step: Optional[NextStep] = Field(default=None, description="The one thing to do about a check that failed, when there is one.", alias="nextStep")
    passing: Optional[StrictBool] = Field(default=None, description="Whether it passed.")
    pending: Optional[StrictBool] = Field(default=None, description="True when the check has not passed because what it checks is still starting or waiting, not because something is wrong. A pending check always has a message: one complete sentence saying what it waits for.")
    __properties: ClassVar[List[str]] = ["idle", "message", "name", "nextStep", "passing", "pending"]

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
        """Create an instance of ClusterAddonHealthCheck from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of next_step
        if self.next_step:
            _dict['nextStep'] = self.next_step.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonHealthCheck from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "idle": obj.get("idle"),
            "message": obj.get("message"),
            "name": obj.get("name"),
            "nextStep": NextStep.from_dict(obj["nextStep"]) if obj.get("nextStep") is not None else None,
            "passing": obj.get("passing"),
            "pending": obj.get("pending")
        })
        return _obj


