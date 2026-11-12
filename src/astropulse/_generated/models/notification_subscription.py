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
from astropulse._generated.models.notification_channel_type import NotificationChannelType
from astropulse._generated.models.notification_topic import NotificationTopic
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class NotificationSubscription(BaseModel):
    """
    NotificationSubscription
    """ # noqa: E501
    channels: Optional[List[NotificationChannelType]] = Field(default=None, description="The channels notifications on the topic are delivered through.")
    created_at: Optional[StrictStr] = Field(default=None, description="When the subscription was created.", alias="createdAt")
    enabled: Optional[StrictBool] = Field(default=None, description="Whether notifications on the topic are delivered.")
    id: Optional[StrictStr] = Field(default=None, description="The identifier of the subscription.")
    org_id: Optional[StrictStr] = Field(default=None, description="The organization the subscription belongs to.", alias="orgId")
    system: Optional[StrictBool] = Field(default=None, description="True for a subscription AstroPulse keeps for every organization.")
    topic: Optional[NotificationTopic] = Field(default=None, description="The notification topic; absent for a topic AstroPulse no longer offers.")
    updated_at: Optional[StrictStr] = Field(default=None, description="When the subscription was last changed.", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["channels", "createdAt", "enabled", "id", "orgId", "system", "topic", "updatedAt"]

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
        """Create an instance of NotificationSubscription from a JSON string"""
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
        """Create an instance of NotificationSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channels": obj.get("channels"),
            "createdAt": obj.get("createdAt"),
            "enabled": obj.get("enabled"),
            "id": obj.get("id"),
            "orgId": obj.get("orgId"),
            "system": obj.get("system"),
            "topic": obj.get("topic"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


