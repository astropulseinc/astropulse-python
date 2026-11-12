# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_addon_tls_challenge import ClusterAddonTLSChallenge
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonTLSChallenges(BaseModel):
    """
    ClusterAddonTLSChallenges
    """ # noqa: E501
    dns01: Optional[ClusterAddonTLSChallenge] = Field(default=None, description="The challenge answered by writing a DNS record, which is what a certificate behind a gateway needs.")
    http01: Optional[ClusterAddonTLSChallenge] = Field(default=None, description="The challenge served over the cluster's ingress.")
    __properties: ClassVar[List[str]] = ["dns01", "http01"]

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
        """Create an instance of ClusterAddonTLSChallenges from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dns01
        if self.dns01:
            _dict['dns01'] = self.dns01.to_dict()
        # override the default output from pydantic by calling `to_dict()` of http01
        if self.http01:
            _dict['http01'] = self.http01.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonTLSChallenges from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dns01": ClusterAddonTLSChallenge.from_dict(obj["dns01"]) if obj.get("dns01") is not None else None,
            "http01": ClusterAddonTLSChallenge.from_dict(obj["http01"]) if obj.get("http01") is not None else None
        })
        return _obj


