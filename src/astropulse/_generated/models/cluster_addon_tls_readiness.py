# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_addon_tls_challenges import ClusterAddonTLSChallenges
from astropulse._generated.models.cluster_addon_tls_exposure import ClusterAddonTLSExposure
from astropulse._generated.models.cluster_addon_tls_issuer import ClusterAddonTLSIssuer
from astropulse._generated.models.cluster_exposure_issuer import ClusterExposureIssuer
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonTLSReadiness(BaseModel):
    """
    ClusterAddonTLSReadiness
    """ # noqa: E501
    challenges: Optional[ClusterAddonTLSChallenges] = Field(default=None, description="Lists the ACME challenge types the Let's Encrypt issuer can solve, and what each still needs when it cannot.")
    cluster_issuer: Optional[ClusterExposureIssuer] = Field(default=None, description="The ClusterIssuer exposure uses on this cluster and what the cluster's agent observed of it. Only on a read of an installed add-on; an apply response has no observation to report.", alias="clusterIssuer")
    exposure: Optional[ClusterAddonTLSExposure] = Field(default=None, description="Says which exposure paths a certificate can be issued for.")
    issuer: Optional[ClusterAddonTLSIssuer] = Field(default=None, description="The AstroPulse ClusterIssuer endpoint certificates come from.")
    notices: Optional[List[Notice]] = Field(default=None, description="Say what stops trusted certificates, or what is worth knowing about the certificates issued, each with the one step to take.")
    trusted_certificates: Optional[StrictBool] = Field(default=None, description="Reports whether certificates browsers and clients trust can be issued on the cluster now.", alias="trustedCertificates")
    __properties: ClassVar[List[str]] = ["challenges", "clusterIssuer", "exposure", "issuer", "notices", "trustedCertificates"]

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
        """Create an instance of ClusterAddonTLSReadiness from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of challenges
        if self.challenges:
            _dict['challenges'] = self.challenges.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cluster_issuer
        if self.cluster_issuer:
            _dict['clusterIssuer'] = self.cluster_issuer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exposure
        if self.exposure:
            _dict['exposure'] = self.exposure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonTLSReadiness from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "challenges": ClusterAddonTLSChallenges.from_dict(obj["challenges"]) if obj.get("challenges") is not None else None,
            "clusterIssuer": ClusterExposureIssuer.from_dict(obj["clusterIssuer"]) if obj.get("clusterIssuer") is not None else None,
            "exposure": ClusterAddonTLSExposure.from_dict(obj["exposure"]) if obj.get("exposure") is not None else None,
            "issuer": obj.get("issuer"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "trustedCertificates": obj.get("trustedCertificates")
        })
        return _obj


