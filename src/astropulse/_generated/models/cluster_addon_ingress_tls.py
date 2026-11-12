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
from astropulse._generated.models.cluster_addon_tls_mode import ClusterAddonTLSMode
from astropulse._generated.models.tls_mode import TLSMode
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonIngressTLS(BaseModel):
    """
    ClusterAddonIngressTLS
    """ # noqa: E501
    app_url: Optional[StrictStr] = Field(default=None, description="Where an application using the wildcard is served, with its name in place of the first label; empty when the wildcard is off.", alias="appUrl")
    default_mode: Optional[TLSMode] = Field(default=None, description="The TLS mode an application gets when it names none and the mode can serve its hostname: Wildcard or Certificate.", alias="defaultMode")
    modes: Optional[List[ClusterAddonTLSMode]] = Field(default=None, description="Lists every TLS mode, whether it is offered and, when it is not, what offers it.")
    passthrough: Optional[StrictBool] = Field(default=None, description="Reports whether an application may serve its own TLS.")
    wildcard_domain: Optional[StrictStr] = Field(default=None, description="The domain the wildcard certificate covers; empty when the wildcard is off.", alias="wildcardDomain")
    wildcard_stale: Optional[StrictStr] = Field(default=None, description="Says why the wildcard certificate no longer matches the cert-manager add-on's issuer, and what to apply; empty when it does.", alias="wildcardStale")
    wildcard_wait: Optional[StrictStr] = Field(default=None, description="Says why the wildcard certificate has not been issued yet; empty once it is.", alias="wildcardWait")
    __properties: ClassVar[List[str]] = ["appUrl", "defaultMode", "modes", "passthrough", "wildcardDomain", "wildcardStale", "wildcardWait"]

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
        """Create an instance of ClusterAddonIngressTLS from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in modes (list)
        _items = []
        if self.modes:
            for _item_modes in self.modes:
                if _item_modes:
                    _items.append(_item_modes.to_dict())
            _dict['modes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonIngressTLS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appUrl": obj.get("appUrl"),
            "defaultMode": obj.get("defaultMode"),
            "modes": [ClusterAddonTLSMode.from_dict(_item) for _item in obj["modes"]] if obj.get("modes") is not None else None,
            "passthrough": obj.get("passthrough"),
            "wildcardDomain": obj.get("wildcardDomain"),
            "wildcardStale": obj.get("wildcardStale"),
            "wildcardWait": obj.get("wildcardWait")
        })
        return _obj


