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
from astropulse._generated.models.cluster_exposure_certificates import ClusterExposureCertificates
from astropulse._generated.models.cluster_exposure_owner import ClusterExposureOwner
from astropulse._generated.models.cluster_issuer_kind import ClusterIssuerKind
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterExposureIssuer(BaseModel):
    """
    ClusterExposureIssuer
    """ # noqa: E501
    certificates: Optional[ClusterExposureCertificates] = Field(default=None, description="What endpoints get from this issuer. Empty when the cluster has no issuer.")
    kind: Optional[ClusterIssuerKind] = Field(default=None, description="How the ClusterIssuer obtains certificates, as the cluster's agent observed it; absent when not observed.")
    message: Optional[StrictStr] = Field(default=None, description="The Ready condition's message, or why the issuer was not observed.")
    name: Optional[StrictStr] = Field(default=None, description="The ClusterIssuer's name; empty when the cluster has none.")
    observed: Optional[StrictBool] = Field(default=None, description="Reports whether the cluster's agent reported this ClusterIssuer.")
    ready: Optional[StrictStr] = Field(default=None, description="The observed Ready condition: True, False or Unknown. Empty when not observed.")
    refusal: Optional[StrictStr] = Field(default=None, description="Empty when an application can be exposed with this issuer now; otherwise the reason a deploy is refused, as the deploy reports it.")
    source: Optional[ClusterExposureOwner] = Field(default=None, description="Platform for the cert-manager add-on's own issuer, Cluster for one named by the cluster's exposure settings, None otherwise.")
    __properties: ClassVar[List[str]] = ["certificates", "kind", "message", "name", "observed", "ready", "refusal", "source"]

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
        """Create an instance of ClusterExposureIssuer from a JSON string"""
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
        """Create an instance of ClusterExposureIssuer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certificates": obj.get("certificates"),
            "kind": obj.get("kind"),
            "message": obj.get("message"),
            "name": obj.get("name"),
            "observed": obj.get("observed"),
            "ready": obj.get("ready"),
            "refusal": obj.get("refusal"),
            "source": obj.get("source")
        })
        return _obj


