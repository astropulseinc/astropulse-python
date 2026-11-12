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
from astropulse._generated.models.cluster_addon_status import ClusterAddonStatus
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.next_step import NextStep
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonSummary(BaseModel):
    """
    ClusterAddonSummary
    """ # noqa: E501
    healthy: Optional[StrictBool] = Field(default=None, description="Whether the add-on's own workload is working; an add-on can be `Deployed` and still not healthy. Absent when its health was not read.")
    message: Optional[StrictStr] = Field(default=None, description="Explains the status in one sentence.")
    next_step: Optional[NextStep] = Field(default=None, description="The one thing to do when the add-on has failed or is not healthy, the same step as notice.nextStep when there is a notice; absent otherwise.", alias="nextStep")
    notice: Optional[Notice] = Field(default=None, description="The add-on's statusNotice: what a failed or unhealthy status means and the one step that resolves it; absent otherwise.")
    overall_status: Optional[ClusterAddonStatus] = Field(default=None, description="Summarises the add-on's health checks in one word, the same value as health.overallStatus on the add-on.", alias="overallStatus")
    status: Optional[ClusterAddonStatus] = Field(default=None, description="Whether the add-on is installed and working.")
    type: Optional[ClusterAddonType] = Field(default=None, description="The add-on's public name, and what every add-on command takes.")
    version: Optional[StrictStr] = Field(default=None, description="The installed chart version.")
    __properties: ClassVar[List[str]] = ["healthy", "message", "nextStep", "notice", "overallStatus", "status", "type", "version"]

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
        """Create an instance of ClusterAddonSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of notice
        if self.notice:
            _dict['notice'] = self.notice.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "healthy": obj.get("healthy"),
            "message": obj.get("message"),
            "nextStep": NextStep.from_dict(obj["nextStep"]) if obj.get("nextStep") is not None else None,
            "notice": Notice.from_dict(obj["notice"]) if obj.get("notice") is not None else None,
            "overallStatus": obj.get("overallStatus"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "version": obj.get("version")
        })
        return _obj


