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
from astropulse._generated.models.addon_auto_scaling_config import AddonAutoScalingConfig
from astropulse._generated.models.endpoint_exposure import EndpointExposure
from astropulse._generated.models.nginx_wildcard_certificate import NginxWildcardCertificate
from astropulse._generated.models.tls_mode import TLSMode
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class NginxAddonConfiguration(BaseModel):
    """
    NginxAddonConfiguration
    """ # noqa: E501
    annotations: Optional[Dict[str, StrictStr]] = Field(default=None, description="Extra annotations on the controller's load balancer Service, for settings your cloud reads from there.")
    auto_scaling: Optional[AddonAutoScalingConfig] = Field(default=None, description="Adds and removes controller copies as load changes.", alias="autoScaling")
    default_tls_mode: Optional[TLSMode] = Field(default=None, description="The TLS mode of an application that names none. Left out, it is `Wildcard` when the wildcard certificate is on and `Certificate` otherwise.", alias="defaultTlsMode")
    enable_node_port: Optional[StrictBool] = Field(default=None, description="Serves the controller on a port of every node instead of a cloud load balancer; turn it on for a cluster that cannot create one.", alias="enableNodePort")
    exposure: Optional[EndpointExposure] = Field(default=None, description="Who can reach the controller's load balancer, and so every application it serves.")
    ingress_class_name: Optional[StrictStr] = Field(default='nginx', description="The ingress class applications use to choose this controller. Left out, it is `nginx`.", alias="ingressClassName")
    node_selector: Optional[StrictStr] = Field(default=None, description="Runs the controller only on nodes with this label, written key=value.", alias="nodeSelector")
    replicas: Optional[StrictInt] = Field(default=None, description="How many copies of the controller run. Left out, AstroPulse's default applies.")
    ssl_passthrough: Optional[StrictBool] = Field(default=None, description="Passes HTTPS through, still encrypted, to applications that serve their own certificate: an application with TLS mode `Passthrough`, or your own Ingress annotated `nginx.ingress.kubernetes.io/ssl-passthrough`. Every other application's HTTPS is decrypted at the controller.", alias="sslPassthrough")
    wildcard_certificate: Optional[NginxWildcardCertificate] = Field(default=None, description="One certificate for a domain and every name directly under it, served to applications with TLS mode `Wildcard`.", alias="wildcardCertificate")
    __properties: ClassVar[List[str]] = ["annotations", "autoScaling", "defaultTlsMode", "enableNodePort", "exposure", "ingressClassName", "nodeSelector", "replicas", "sslPassthrough", "wildcardCertificate"]

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
        """Create an instance of NginxAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auto_scaling
        if self.auto_scaling:
            _dict['autoScaling'] = self.auto_scaling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wildcard_certificate
        if self.wildcard_certificate:
            _dict['wildcardCertificate'] = self.wildcard_certificate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NginxAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "annotations": obj.get("annotations"),
            "autoScaling": AddonAutoScalingConfig.from_dict(obj["autoScaling"]) if obj.get("autoScaling") is not None else None,
            "defaultTlsMode": obj.get("defaultTlsMode"),
            "enableNodePort": obj.get("enableNodePort"),
            "exposure": obj.get("exposure"),
            "ingressClassName": obj.get("ingressClassName") if obj.get("ingressClassName") is not None else 'nginx',
            "nodeSelector": obj.get("nodeSelector"),
            "replicas": obj.get("replicas"),
            "sslPassthrough": obj.get("sslPassthrough"),
            "wildcardCertificate": NginxWildcardCertificate.from_dict(obj["wildcardCertificate"]) if obj.get("wildcardCertificate") is not None else None
        })
        return _obj


