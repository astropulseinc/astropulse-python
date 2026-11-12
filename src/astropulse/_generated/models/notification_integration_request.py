# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.notification_channel_type import NotificationChannelType
from astropulse._generated.models.notification_integration_config_request import NotificationIntegrationConfigRequest
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class NotificationIntegrationRequest(BaseModel):
    """
    NotificationIntegrationRequest
    """ # noqa: E501
    channel: Optional[NotificationChannelType] = Field(default=None, description="The channel notifications are delivered through.")
    config: Optional[NotificationIntegrationConfigRequest] = Field(default=None, description="The channel's settings.")
    enabled: Optional[StrictBool] = Field(default=None, description="Whether notifications are delivered through this channel.")
    __properties: ClassVar[List[str]] = ["channel", "config", "enabled"]

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
        """Create an instance of NotificationIntegrationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationIntegrationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channel": obj.get("channel"),
            "config": NotificationIntegrationConfigRequest.from_dict(obj["config"]) if obj.get("config") is not None else None,
            "enabled": obj.get("enabled")
        })
        return _obj


