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
from astropulse._generated.models.app_resource import AppResource
from astropulse._generated.models.availability_tier import AvailabilityTier
from astropulse._generated.models.network_traffic import NetworkTraffic
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Constraints(BaseModel):
    """
    Constraints
    """ # noqa: E501
    availability: Optional[AvailabilityTier] = None
    network_traffic: Optional[NetworkTraffic] = Field(default=None, alias="networkTraffic")
    resources: Optional[AppResource] = None
    __properties: ClassVar[List[str]] = ["availability", "networkTraffic", "resources"]

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
        """Create an instance of Constraints from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of availability
        if self.availability:
            _dict['availability'] = self.availability.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network_traffic
        if self.network_traffic:
            _dict['networkTraffic'] = self.network_traffic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Constraints from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availability": AvailabilityTier.from_dict(obj["availability"]) if obj.get("availability") is not None else None,
            "networkTraffic": NetworkTraffic.from_dict(obj["networkTraffic"]) if obj.get("networkTraffic") is not None else None,
            "resources": AppResource.from_dict(obj["resources"]) if obj.get("resources") is not None else None
        })
        return _obj


