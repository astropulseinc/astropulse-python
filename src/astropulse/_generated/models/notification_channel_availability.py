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
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.notification_channel_type import NotificationChannelType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class NotificationChannelAvailability(BaseModel):
    """
    NotificationChannelAvailability
    """ # noqa: E501
    channel: Optional[NotificationChannelType] = Field(default=None, description="The delivery channel.")
    current_plan: Optional[StrictStr] = Field(default=None, description="The organization's plan.", alias="currentPlan")
    included_in_plan: Optional[StrictBool] = Field(default=None, description="True when the organization's plan includes the channel.", alias="includedInPlan")
    notice: Optional[Notice] = Field(default=None, description="Says which plan includes the channel and how to upgrade to it; absent when the current plan includes it.")
    required_plan: Optional[StrictStr] = Field(default=None, description="The plan that includes the channel, set when the current plan does not.", alias="requiredPlan")
    __properties: ClassVar[List[str]] = ["channel", "currentPlan", "includedInPlan", "notice", "requiredPlan"]

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
        """Create an instance of NotificationChannelAvailability from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of notice
        if self.notice:
            _dict['notice'] = self.notice.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationChannelAvailability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channel": obj.get("channel"),
            "currentPlan": obj.get("currentPlan"),
            "includedInPlan": obj.get("includedInPlan"),
            "notice": Notice.from_dict(obj["notice"]) if obj.get("notice") is not None else None,
            "requiredPlan": obj.get("requiredPlan")
        })
        return _obj


