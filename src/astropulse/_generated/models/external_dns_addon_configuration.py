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
from astropulse._generated.models.cloud_access_mode import CloudAccessMode
from astropulse._generated.models.external_dns_policy import ExternalDNSPolicy
from astropulse._generated.models.external_dns_provider import ExternalDNSProvider
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ExternalDNSAddonConfiguration(BaseModel):
    """
    ExternalDNSAddonConfiguration
    """ # noqa: E501
    cloud_access: Optional[CloudAccessMode] = Field(default=None, description="How external-dns signs in to your DNS provider. Left out, it is `Identity` when `identity` is set, `Secret` when `secretRef` is set, and `None` otherwise.", alias="cloudAccess")
    domain_filter: Optional[StrictStr] = Field(default=None, description="The DNS zones external-dns may change, such as example.com, separated by commas. Left out, it is your organization's verified domains when it runs as the identity AstroPulse created (refused if you have none), and otherwise every zone its credentials reach.", alias="domainFilter")
    dry_run: Optional[StrictBool] = Field(default=None, description="Logs the DNS changes external-dns would make without making them.", alias="dryRun")
    gateway_routes: Optional[StrictBool] = Field(default=None, description="Also publishes DNS for the hostnames of Gateway API routes, not only Ingress hostnames; needs the Gateway API on the cluster.", alias="gatewayRoutes")
    identity: Optional[AddonWorkloadIdentity] = Field(default=None, description="The cloud identity external-dns runs as to change records in your DNS zone. On an EKS cluster AstroPulse created it defaults to the role made for it; on a registered cluster using Route 53, set this or `secretRef`.")
    policy: Optional[ExternalDNSPolicy] = Field(default=None, description="What external-dns may do to the records it owns. Left out, an update keeps the current value and a new add-on uses `Sync`.")
    provider: Optional[ExternalDNSProvider] = Field(default=None, description="The DNS service that holds your zone. Left out, it is the cluster's own cloud, and refused when that is not known.")
    secret_ref: Optional[StrictStr] = Field(default=None, description="The name of a Secret in the add-on's namespace holding DNS provider credentials. Use it only where a cloud identity can't be used, such as a zone in another cloud; it can't be combined with `identity`.", alias="secretRef")
    txt_owner_id: Optional[StrictStr] = Field(default=None, description="The owner name written on this cluster's DNS records, so clusters sharing a zone leave each other's records alone. Left out, it keeps the current value, or on a first install is made from the cluster's name.", alias="txtOwnerId")
    __properties: ClassVar[List[str]] = ["cloudAccess", "domainFilter", "dryRun", "gatewayRoutes", "identity", "policy", "provider", "secretRef", "txtOwnerId"]

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
        """Create an instance of ExternalDNSAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalDNSAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudAccess": obj.get("cloudAccess"),
            "domainFilter": obj.get("domainFilter"),
            "dryRun": obj.get("dryRun"),
            "gatewayRoutes": obj.get("gatewayRoutes"),
            "identity": AddonWorkloadIdentity.from_dict(obj["identity"]) if obj.get("identity") is not None else None,
            "policy": obj.get("policy"),
            "provider": obj.get("provider"),
            "secretRef": obj.get("secretRef"),
            "txtOwnerId": obj.get("txtOwnerId")
        })
        return _obj


