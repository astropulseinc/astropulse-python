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
from astropulse._generated.models.endpoint_exposure_status import EndpointExposureStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterLoadBalancerExposure(BaseModel):
    """
    ClusterLoadBalancerExposure
    """ # noqa: E501
    gateway_default: Optional[EndpointExposureStatus] = Field(default=None, description="The exposure a model endpoint on the gateway takes when it names none, the gateway add-on's; absent without the add-on.", alias="gatewayDefault")
    gateway_private: Optional[StrictBool] = Field(default=None, description="Reports whether the gateway add-on serves private model endpoints beside public ones.", alias="gatewayPrivate")
    ingress_default: Optional[EndpointExposureStatus] = Field(default=None, description="The exposure of every Ingress endpoint, the nginx-ingress add-on's; absent without the add-on.", alias="ingressDefault")
    load_balancer_default: Optional[EndpointExposureStatus] = Field(default=None, description="The exposure an application with accessType LoadBalancer takes when it names none: public.", alias="loadBalancerDefault")
    note: Optional[StrictStr] = Field(default=None, description="A sentence about the cluster's load balancers, for example that every one is a Network Load Balancer on AWS.")
    private_available: Optional[StrictBool] = Field(default=None, description="Reports whether this cluster can serve a private endpoint at all.", alias="privateAvailable")
    private_refusal: Optional[StrictStr] = Field(default=None, description="Why a private endpoint is refused on this cluster; empty when one can be served.", alias="privateRefusal")
    __properties: ClassVar[List[str]] = ["gatewayDefault", "gatewayPrivate", "ingressDefault", "loadBalancerDefault", "note", "privateAvailable", "privateRefusal"]

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
        """Create an instance of ClusterLoadBalancerExposure from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gateway_default
        if self.gateway_default:
            _dict['gatewayDefault'] = self.gateway_default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ingress_default
        if self.ingress_default:
            _dict['ingressDefault'] = self.ingress_default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of load_balancer_default
        if self.load_balancer_default:
            _dict['loadBalancerDefault'] = self.load_balancer_default.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterLoadBalancerExposure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gatewayDefault": EndpointExposureStatus.from_dict(obj["gatewayDefault"]) if obj.get("gatewayDefault") is not None else None,
            "gatewayPrivate": obj.get("gatewayPrivate"),
            "ingressDefault": EndpointExposureStatus.from_dict(obj["ingressDefault"]) if obj.get("ingressDefault") is not None else None,
            "loadBalancerDefault": EndpointExposureStatus.from_dict(obj["loadBalancerDefault"]) if obj.get("loadBalancerDefault") is not None else None,
            "note": obj.get("note"),
            "privateAvailable": obj.get("privateAvailable"),
            "privateRefusal": obj.get("privateRefusal")
        })
        return _obj


