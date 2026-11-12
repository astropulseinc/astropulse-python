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
from astropulse._generated.models.setup_step_state import SetupStepState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SetupStep(BaseModel):
    """
    SetupStep
    """ # noqa: E501
    cloud_error: Optional[StrictStr] = Field(default=None, description="The cloud provider's own error when the step failed.", alias="cloudError")
    name: Optional[StrictStr] = Field(default=None, description="The step's stable ID: plan, template, create, verify or store.")
    reason: Optional[StrictStr] = Field(default=None, description="Says what happened or what the step waits for.")
    state: Optional[SetupStepState] = Field(default=None, description="Where the step stands.")
    title: Optional[StrictStr] = Field(default=None, description="Says what the step does.")
    updated_at: Optional[StrictStr] = Field(default=None, description="When the step last changed.", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["cloudError", "name", "reason", "state", "title", "updatedAt"]

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
        """Create an instance of SetupStep from a JSON string"""
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
        """Create an instance of SetupStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudError": obj.get("cloudError"),
            "name": obj.get("name"),
            "reason": obj.get("reason"),
            "state": obj.get("state"),
            "title": obj.get("title"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


