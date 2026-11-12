# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.addon_resources import AddonResources
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AddonResourceRequirements(BaseModel):
    """
    AddonResourceRequirements
    """ # noqa: E501
    limits: Optional[AddonResources] = Field(default=None, description="The most CPU and memory the component may use, at least `requests`. Where AstroPulse sets a limit and you set none, the memory request is also the memory limit and the CPU limit is at least the CPU request; set `limits` to make them differ.")
    requests: Optional[AddonResources] = Field(default=None, description="The CPU and memory set aside for the component. Left out, an update keeps the current values and a new add-on gets AstroPulse's sizing.")
    __properties: ClassVar[List[str]] = ["limits", "requests"]

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
        """Create an instance of AddonResourceRequirements from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requests
        if self.requests:
            _dict['requests'] = self.requests.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddonResourceRequirements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limits": AddonResources.from_dict(obj["limits"]) if obj.get("limits") is not None else None,
            "requests": AddonResources.from_dict(obj["requests"]) if obj.get("requests") is not None else None
        })
        return _obj


