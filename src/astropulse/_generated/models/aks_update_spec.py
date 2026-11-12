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
from typing_extensions import Annotated
from astropulse._generated.models.aks_auto_upgrade_channel import AKSAutoUpgradeChannel
from astropulse._generated.models.aks_node_os_upgrade_channel import AKSNodeOSUpgradeChannel
from astropulse._generated.models.credentials import Credentials
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AKSUpdateSpec(BaseModel):
    """
    AKSUpdateSpec
    """ # noqa: E501
    acr_resource_ids: Optional[Annotated[List[StrictStr], Field(max_length=20)]] = Field(default=None, description="Replaces the registries the cluster pulls from with no credential (optional, max 20): added ones get AcrPull, removed ones lose it. Omit to keep them.", alias="acrResourceIds")
    authorized_ip_ranges: Optional[Annotated[List[StrictStr], Field(max_length=200)]] = Field(default=None, description="CIDR blocks that restrict API server access (optional, max 200 entries). Each entry must be a valid CIDR block. Not supported for private clusters.", alias="authorizedIPRanges")
    auto_upgrade_channel: Optional[AKSAutoUpgradeChannel] = Field(default=None, description="How the cluster upgrades its Kubernetes version. Omitted keeps it.", alias="autoUpgradeChannel")
    credentials: Optional[Credentials] = Field(default=None, description="Replaces the cluster's stored static credentials when it carries data; omitted, or with the type and no data, it keeps them.")
    node_os_upgrade_channel: Optional[AKSNodeOSUpgradeChannel] = Field(default=None, description="How the cluster updates its nodes' operating system. Omitted keeps it.", alias="nodeOsUpgradeChannel")
    __properties: ClassVar[List[str]] = ["acrResourceIds", "authorizedIPRanges", "autoUpgradeChannel", "credentials", "nodeOsUpgradeChannel"]

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
        """Create an instance of AKSUpdateSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AKSUpdateSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "acrResourceIds": obj.get("acrResourceIds"),
            "authorizedIPRanges": obj.get("authorizedIPRanges"),
            "autoUpgradeChannel": obj.get("autoUpgradeChannel"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "nodeOsUpgradeChannel": obj.get("nodeOsUpgradeChannel")
        })
        return _obj


