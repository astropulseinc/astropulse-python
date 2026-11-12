# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.endpoint_desired_state import EndpointDesiredState
from astropulse._generated.models.endpoint_dns_observation import EndpointDNSObservation
from astropulse._generated.models.endpoint_origin import EndpointOrigin
from astropulse._generated.models.endpoint_phase import EndpointPhase
from astropulse._generated.models.endpoint_probe import EndpointProbe
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class EndpointStatus(BaseModel):
    """
    EndpointStatus
    """ # noqa: E501
    allowed_origins: Optional[List[EndpointOrigin]] = Field(default=None, description="The websites whose pages can call the endpoint from a browser, each with where it comes from. Reported only while URL is reported.", alias="allowedOrigins")
    application: Optional[StrictStr] = None
    cluster: Optional[StrictStr] = None
    desired_state: Optional[EndpointDesiredState] = Field(default=None, alias="desiredState")
    dns: Optional[EndpointDNSObservation] = Field(default=None, description="What AstroPulse observed of the endpoint's hostname: whether it resolves, and whether that is the address the cluster's gateway publishes. Only reported while URL is reported.")
    generation: Optional[StrictInt] = None
    message: Optional[StrictStr] = Field(default=None, description="Says in plain words why the endpoint is Pending or in Error, or on Ready what a caller must send, how far its address was checked and any warning about it.")
    notices: Optional[List[Notice]] = Field(default=None, description="What to do about the endpoint's state, each with its next step.")
    observed_at: Optional[StrictStr] = Field(default=None, alias="observedAt")
    phase: Optional[EndpointPhase] = None
    policy: Optional[StrictStr] = None
    policy_revision: Optional[StrictInt] = Field(default=None, alias="policyRevision")
    probe: Optional[EndpointProbe] = None
    url: Optional[StrictStr] = Field(default=None, description="The address to call. It is shown while the endpoint is open and Ready, and is empty otherwise; message says how far the address was checked.")
    __properties: ClassVar[List[str]] = ["allowedOrigins", "application", "cluster", "desiredState", "dns", "generation", "message", "notices", "observedAt", "phase", "policy", "policyRevision", "probe", "url"]

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
        """Create an instance of EndpointStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_origins (list)
        _items = []
        if self.allowed_origins:
            for _item_allowed_origins in self.allowed_origins:
                if _item_allowed_origins:
                    _items.append(_item_allowed_origins.to_dict())
            _dict['allowedOrigins'] = _items
        # override the default output from pydantic by calling `to_dict()` of dns
        if self.dns:
            _dict['dns'] = self.dns.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        # override the default output from pydantic by calling `to_dict()` of probe
        if self.probe:
            _dict['probe'] = self.probe.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedOrigins": [EndpointOrigin.from_dict(_item) for _item in obj["allowedOrigins"]] if obj.get("allowedOrigins") is not None else None,
            "application": obj.get("application"),
            "cluster": obj.get("cluster"),
            "desiredState": obj.get("desiredState"),
            "dns": EndpointDNSObservation.from_dict(obj["dns"]) if obj.get("dns") is not None else None,
            "generation": obj.get("generation"),
            "message": obj.get("message"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "observedAt": obj.get("observedAt"),
            "phase": obj.get("phase"),
            "policy": obj.get("policy"),
            "policyRevision": obj.get("policyRevision"),
            "probe": EndpointProbe.from_dict(obj["probe"]) if obj.get("probe") is not None else None,
            "url": obj.get("url")
        })
        return _obj


