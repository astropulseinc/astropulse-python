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
from astropulse._generated.models.next_step import NextStep
from astropulse._generated.models.notice_code import NoticeCode
from astropulse._generated.models.notice_severity import NoticeSeverity
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Notice(BaseModel):
    """
    Notice
    """ # noqa: E501
    code: Optional[NoticeCode] = Field(default=None, description="Identifies the notice and is unique across the API.")
    hostname: Optional[StrictStr] = Field(default=None, description="The hostname the application is served at, on a `HostnameTaken` notice.")
    message: Optional[StrictStr] = Field(default=None, description="Says in one or two sentences what happened and why.")
    next_step: Optional[NextStep] = Field(default=None, description="The one thing to do, when there is one.", alias="nextStep")
    preferred: Optional[StrictStr] = Field(default=None, description="The hostname that was taken, on a `HostnameTaken` notice.")
    severity: Optional[NoticeSeverity] = Field(default=None, description="How much the notice matters.")
    title: Optional[StrictStr] = Field(default=None, description="A short headline of at most 60 characters.")
    __properties: ClassVar[List[str]] = ["code", "hostname", "message", "nextStep", "preferred", "severity", "title"]

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
        """Create an instance of Notice from a JSON string"""
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
        """Create an instance of Notice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "hostname": obj.get("hostname"),
            "message": obj.get("message"),
            "nextStep": NextStep.from_dict(obj["nextStep"]) if obj.get("nextStep") is not None else None,
            "preferred": obj.get("preferred"),
            "severity": obj.get("severity"),
            "title": obj.get("title")
        })
        return _obj


