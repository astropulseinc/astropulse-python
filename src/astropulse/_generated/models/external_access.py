# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.endpoint_access_policy_reference import EndpointAccessPolicyReference
from astropulse._generated.models.endpoint_exposure import EndpointExposure
from astropulse._generated.models.external_access_tls import ExternalAccessTLS
from astropulse._generated.models.external_access_type import ExternalAccessType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ExternalAccess(BaseModel):
    """
    ExternalAccess
    """ # noqa: E501
    access_policy_ref: Optional[EndpointAccessPolicyReference] = Field(default=None, alias="accessPolicyRef")
    access_type: Optional[ExternalAccessType] = Field(default=None, description="Defines the external access type", alias="accessType")
    dns_endpoint: Optional[StrictStr] = Field(default=None, description="The resolved served hostname. For image and model applications it is derived from domain/hostname. For Helm and repository applications it is the hostname the chart serves, shown for reference. example: sub.domain.com", alias="dnsEndpoint")
    domain: Optional[StrictStr] = Field(default=None, description="(image and model applications): a verified domain to generate the app's hostname under; the app is served at <app>.<domain>. Mutually exclusive with hostname. example: example.com")
    exposure: Optional[EndpointExposure] = Field(default=None, description="Who can reach the endpoint: Public (from the internet) or Private (only from inside the cluster's network). Omitted takes the default of the path that serves it: the nginx-ingress or gateway add-on's exposure, or Public for a LoadBalancer.")
    hostname: Optional[StrictStr] = Field(default=None, description="(image and model applications): serve the app at exactly this hostname — a verified domain's apex, or a hostname under a verified domain. Mutually exclusive with domain. example: shop.example.com")
    tls: Optional[ExternalAccessTLS] = Field(default=None, description="(applications exposed through Ingress) is how the endpoint's TLS is served. Omitted takes the default of the cluster's nginx-ingress add-on; a model application takes Certificate only.")
    __properties: ClassVar[List[str]] = ["accessPolicyRef", "accessType", "dnsEndpoint", "domain", "exposure", "hostname", "tls"]

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
        """Create an instance of ExternalAccess from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_policy_ref
        if self.access_policy_ref:
            _dict['accessPolicyRef'] = self.access_policy_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tls
        if self.tls:
            _dict['tls'] = self.tls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalAccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessPolicyRef": EndpointAccessPolicyReference.from_dict(obj["accessPolicyRef"]) if obj.get("accessPolicyRef") is not None else None,
            "accessType": obj.get("accessType"),
            "dnsEndpoint": obj.get("dnsEndpoint"),
            "domain": obj.get("domain"),
            "exposure": obj.get("exposure"),
            "hostname": obj.get("hostname"),
            "tls": ExternalAccessTLS.from_dict(obj["tls"]) if obj.get("tls") is not None else None
        })
        return _obj


