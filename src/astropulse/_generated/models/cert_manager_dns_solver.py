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
from astropulse._generated.models.cert_manager_dns_provider import CertManagerDNSProvider
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CertManagerDNSSolver(BaseModel):
    """
    CertManagerDNSSolver
    """ # noqa: E501
    hosted_zone_id: Optional[StrictStr] = Field(default=None, description="The Route 53 hosted zone to use. Left out, cert-manager finds the zone by name.", alias="hostedZoneId")
    project: Optional[StrictStr] = Field(default=None, description="The Google Cloud project that holds the Cloud DNS zone. Required for `gcp`.")
    provider: Optional[CertManagerDNSProvider] = Field(default=None, description="The DNS service that holds the zone. Left out, it is the cluster's own cloud.")
    resource_group: Optional[StrictStr] = Field(default=None, description="The Azure resource group that holds the DNS zone. Required for `azure`.", alias="resourceGroup")
    subscription_id: Optional[StrictStr] = Field(default=None, description="The Azure subscription that holds the DNS zone. Required for `azure`.", alias="subscriptionId")
    __properties: ClassVar[List[str]] = ["hostedZoneId", "project", "provider", "resourceGroup", "subscriptionId"]

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
        """Create an instance of CertManagerDNSSolver from a JSON string"""
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
        """Create an instance of CertManagerDNSSolver from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostedZoneId": obj.get("hostedZoneId"),
            "project": obj.get("project"),
            "provider": obj.get("provider"),
            "resourceGroup": obj.get("resourceGroup"),
            "subscriptionId": obj.get("subscriptionId")
        })
        return _obj


