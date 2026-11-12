# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.error_code import ErrorCode
from astropulse._generated.models.next_step import NextStep
from astropulse._generated.models.notice_severity import NoticeSeverity
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ErrorResponse(BaseModel):
    """
    Standard error response format for API errors
    """ # noqa: E501
    code: Optional[ErrorCode] = Field(default=None, description="The kind of failure, one of a few values shared by every route. Match on it.")
    details: Optional[Dict[str, Any]] = Field(default=None, description="Carries structured context for the code. For an Invalid request, details.fields lists every refused field as {field, rule, reason}: its path in the request body (such as dataPlane.nodeGroups[0].labels[\"team.example.com/owner\"], empty for the body as a whole), the rule it broke and what that rule requires.")
    message: Optional[StrictStr] = Field(default=None, description="What went wrong, in human-readable form. Do not match on it; match on code.", json_schema_extra={"examples": ["Cluster 'prod-eu' not found"]})
    next_step: Optional[NextStep] = Field(default=None, description="The one thing to do about the error, when there is one.", alias="nextStep")
    reason: Optional[StrictStr] = Field(default=None, description="Which failure it was, such as ClusterNotFound: an error reason, or on an error that says what to do next, its notice code.", json_schema_extra={"examples": ["ClusterNotFound"]})
    severity: Optional[NoticeSeverity] = Field(default=None, description="How much the error matters: the severity of the notice it carries; Blocking for an error that names a next step without a notice, and absent for one with neither.")
    status: Optional[StrictInt] = Field(default=None, description="The HTTP status code, repeated here for clients that keep only the body.", json_schema_extra={"examples": [404]})
    title: Optional[StrictStr] = Field(default=None, description="A short headline for the error, when it says what to do next.")
    trace_id: Optional[StrictStr] = Field(default=None, description="Identifies this request and is also returned in the X-Trace-ID header. Quote it in a bug report.", alias="traceId", json_schema_extra={"examples": ["4b1d8f2a9c3e5f70"]})
    __properties: ClassVar[List[str]] = ["code", "details", "message", "nextStep", "reason", "severity", "status", "title", "traceId"]

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
        """Create an instance of ErrorResponse from a JSON string"""
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
        """Create an instance of ErrorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "details": obj.get("details"),
            "message": obj.get("message"),
            "nextStep": NextStep.from_dict(obj["nextStep"]) if obj.get("nextStep") is not None else None,
            "reason": obj.get("reason"),
            "severity": obj.get("severity"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "traceId": obj.get("traceId")
        })
        return _obj


