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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class EndpointDNSObservation(BaseModel):
    """
    EndpointDNSObservation
    """ # noqa: E501
    addresses: Optional[List[StrictStr]] = Field(default=None, description="The IP addresses the hostname resolved to.")
    exposure_addresses: Optional[List[StrictStr]] = Field(default=None, description="The addresses the cluster's exposure publishes (the gateway's or the ingress controller's load balancer), the ones the hostname must point at. Empty when the exposure has no public address (NodePort).", alias="exposureAddresses")
    hostname: Optional[StrictStr] = Field(default=None, description="The exposed hostname that was resolved.")
    matches: Optional[StrictBool] = Field(default=None, description="Reports whether the hostname resolves to one of the exposure's addresses. Absent when there is nothing to compare: the hostname does not resolve, or the exposure publishes no address.")
    message: Optional[StrictStr] = Field(default=None, description="Says what could not be compared, or why.")
    resolves: Optional[StrictBool] = Field(default=None, description="Reports whether the hostname resolved to at least one address.")
    __properties: ClassVar[List[str]] = ["addresses", "exposureAddresses", "hostname", "matches", "message", "resolves"]

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
        """Create an instance of EndpointDNSObservation from a JSON string"""
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
        """Create an instance of EndpointDNSObservation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addresses": obj.get("addresses"),
            "exposureAddresses": obj.get("exposureAddresses"),
            "hostname": obj.get("hostname"),
            "matches": obj.get("matches"),
            "message": obj.get("message"),
            "resolves": obj.get("resolves")
        })
        return _obj


