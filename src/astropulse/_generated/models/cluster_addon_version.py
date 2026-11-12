# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_addon_support import ClusterAddonSupport
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonVersion(BaseModel):
    """
    ClusterAddonVersion
    """ # noqa: E501
    breaking_changes: Optional[List[StrictStr]] = Field(default=None, description="Lists what this release changes incompatibly. It is the reason to read this list before choosing a version: add-ons run in the cluster's critical path -- NGINX carries live traffic, Karpenter owns node lifecycle -- so an upgrade is not something to pick from a version number alone. Empty means the release declares none, not that none were checked.", alias="breakingChanges")
    default: Optional[StrictBool] = Field(default=None, description="Marks the version installed when none is named.")
    endpoint_authentication: Optional[List[StrictStr]] = Field(default=None, description="Lists the access-policy mechanisms this version enforces on the endpoints it routes. Empty when it enforces none.", alias="endpointAuthentication")
    kubernetes_compatibility: Optional[List[StrictStr]] = Field(default=None, description="Lists the Kubernetes minors this version runs on.", alias="kubernetesCompatibility")
    release_date: Optional[datetime] = Field(default=None, description="When this version was published, RFC 3339.", alias="releaseDate")
    release_notes: Optional[StrictStr] = Field(default=None, description="Links or summarises what changed in this version.", alias="releaseNotes")
    stable: Optional[StrictBool] = Field(default=None, description="True for a recommended or supported version, and false once it is deprecated.")
    support: Optional[ClusterAddonSupport] = Field(default=None, description="Says whether this version is supported and until when. Absent when the version's lifecycle is not known.")
    upstream_version: Optional[StrictStr] = Field(default=None, description="The third-party release this version runs, such as \"cert-manager v1.21.2\" or \"KServe v0.20.0\". Empty when there is none.", alias="upstreamVersion")
    version: Optional[StrictStr] = Field(default=None, description="The add-on version, and what `apply --version` takes.")
    __properties: ClassVar[List[str]] = ["breakingChanges", "default", "endpointAuthentication", "kubernetesCompatibility", "releaseDate", "releaseNotes", "stable", "support", "upstreamVersion", "version"]

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
        """Create an instance of ClusterAddonVersion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of support
        if self.support:
            _dict['support'] = self.support.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "breakingChanges": obj.get("breakingChanges"),
            "default": obj.get("default"),
            "endpointAuthentication": obj.get("endpointAuthentication"),
            "kubernetesCompatibility": obj.get("kubernetesCompatibility"),
            "releaseDate": obj.get("releaseDate"),
            "releaseNotes": obj.get("releaseNotes"),
            "stable": obj.get("stable"),
            "support": ClusterAddonSupport.from_dict(obj["support"]) if obj.get("support") is not None else None,
            "upstreamVersion": obj.get("upstreamVersion"),
            "version": obj.get("version")
        })
        return _obj


