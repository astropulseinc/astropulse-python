# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.outcome import Outcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationDeployment(BaseModel):
    """
    ApplicationDeployment
    """ # noqa: E501
    created: Optional[StrictBool] = Field(default=None, description="False when the deploy updated an application that already existed.")
    name: Optional[StrictStr] = Field(default=None, description="The application, and what every other endpoint takes.")
    notices: Optional[List[Notice]] = Field(default=None, description="Say what the deploy did differently from what the request asked; absent when there is nothing to say.")
    outcome: Optional[Outcome] = Field(default=None, description="Proceed: the deploy went ahead.")
    profile_name: Optional[StrictStr] = Field(default=None, description="The profile the application deployed onto.", alias="profileName")
    version: Optional[StrictInt] = Field(default=None, description="The application version this deploy recorded, and what a rollback returns to.")
    __properties: ClassVar[List[str]] = ["created", "name", "notices", "outcome", "profileName", "version"]

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
        """Create an instance of ApplicationDeployment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationDeployment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "name": obj.get("name"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "outcome": obj.get("outcome"),
            "profileName": obj.get("profileName"),
            "version": obj.get("version")
        })
        return _obj


