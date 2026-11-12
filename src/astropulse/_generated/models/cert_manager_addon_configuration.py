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
from astropulse._generated.models.addon_workload_identity import AddonWorkloadIdentity
from astropulse._generated.models.cert_manager_dns_solver import CertManagerDNSSolver
from astropulse._generated.models.cert_manager_issuer_type import CertManagerIssuerType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CertManagerAddonConfiguration(BaseModel):
    """
    CertManagerAddonConfiguration
    """ # noqa: E501
    dns_solver: Optional[CertManagerDNSSolver] = Field(default=None, description="Proves domain ownership to Let's Encrypt through your DNS zone, for applications behind an Ingress or the gateway; without it, Ingress certificates are proven over HTTP. Needs a Let's Encrypt issuer, and on an EKS cluster AstroPulse created defaults to the cluster's Route 53 zones.", alias="dnsSolver")
    email: Optional[StrictStr] = Field(default=None, description="The address Let's Encrypt registers your account under and sends expiry notices to. Required for the Let's Encrypt issuers.")
    enable_cluster_issuer: Optional[StrictBool] = Field(default=True, description="Creates AstroPulse's certificate issuers; turn it off to install cert-manager without issuing anything.", alias="enableClusterIssuer")
    identity: Optional[AddonWorkloadIdentity] = Field(default=None, description="The cloud identity cert-manager runs as to answer ownership checks in your DNS zone. Required with `dnsSolver`, except on an EKS cluster AstroPulse created, where it defaults to the role made for it.")
    install_crds: Optional[StrictBool] = Field(default=True, description="Installs cert-manager's resource definitions with the add-on; turn it off only if you manage them yourself.", alias="installCRDs")
    issuer_type: Optional[CertManagerIssuerType] = Field(default=None, description="Where certificates come from. Left out, it is `LetsEncrypt` once `email` is set; with no email, no issuer is created.", alias="issuerType")
    __properties: ClassVar[List[str]] = ["dnsSolver", "email", "enableClusterIssuer", "identity", "installCRDs", "issuerType"]

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
        """Create an instance of CertManagerAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dns_solver
        if self.dns_solver:
            _dict['dnsSolver'] = self.dns_solver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CertManagerAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dnsSolver": CertManagerDNSSolver.from_dict(obj["dnsSolver"]) if obj.get("dnsSolver") is not None else None,
            "email": obj.get("email"),
            "enableClusterIssuer": obj.get("enableClusterIssuer") if obj.get("enableClusterIssuer") is not None else True,
            "identity": AddonWorkloadIdentity.from_dict(obj["identity"]) if obj.get("identity") is not None else None,
            "installCRDs": obj.get("installCRDs") if obj.get("installCRDs") is not None else True,
            "issuerType": obj.get("issuerType")
        })
        return _obj


