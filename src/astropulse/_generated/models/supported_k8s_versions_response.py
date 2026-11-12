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
from astropulse._generated.models.ami_families_for_version import AMIFamiliesForVersion
from astropulse._generated.models.channel_versions import ChannelVersions
from astropulse._generated.models.failure import Failure
from astropulse._generated.models.k8s_upgrade_path import K8sUpgradePath
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.version_floor_source import VersionFloorSource
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SupportedK8sVersionsResponse(BaseModel):
    """
    SupportedK8sVersionsResponse
    """ # noqa: E501
    ami_families: Optional[List[AMIFamiliesForVersion]] = Field(default=None, description="Lists, for each Kubernetes minor version, the AMI families an EKS node group can use (EKS only).", alias="amiFamilies")
    ami_families_notice: Optional[Notice] = Field(default=None, description="Says why amiFamilies is absent when the AMI families could not be checked (EKS only).", alias="amiFamiliesNotice")
    channel_versions: Optional[Dict[str, ChannelVersions]] = Field(default=None, description="The versions of each GKE release channel, keyed by channel: `Stable`, `Regular` or `Rapid` (GKE only).", alias="channelVersions")
    default_version: Optional[StrictStr] = Field(default=None, description="The version a create uses when it names none.", alias="defaultVersion")
    default_version_reason: Optional[StrictStr] = Field(default=None, description="How `defaultVersion` is chosen, in one sentence.", alias="defaultVersionReason")
    error: Optional[Failure] = Field(default=None, description="Contains any error message if the request failed")
    limited_by: Optional[VersionFloorSource] = Field(default=None, description="What sets the oldest supported version.", alias="limitedBy")
    minimum_version: Optional[StrictStr] = Field(default=None, description="The oldest Kubernetes minor series in supportedVersions, for example \"1.34\". It summarises the list and does not replace it: a newer version is supported only if it appears in supportedVersions.", alias="minimumVersion")
    supported_versions: Optional[List[StrictStr]] = Field(default=None, description="A list of supported K8s versions in semver format", alias="supportedVersions")
    upgrade_paths: Optional[List[K8sUpgradePath]] = Field(default=None, description="Contains available upgrade paths from current version", alias="upgradePaths")
    __properties: ClassVar[List[str]] = ["amiFamilies", "amiFamiliesNotice", "channelVersions", "defaultVersion", "defaultVersionReason", "error", "limitedBy", "minimumVersion", "supportedVersions", "upgradePaths"]

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
        """Create an instance of SupportedK8sVersionsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ami_families (list)
        _items = []
        if self.ami_families:
            for _item_ami_families in self.ami_families:
                if _item_ami_families:
                    _items.append(_item_ami_families.to_dict())
            _dict['amiFamilies'] = _items
        # override the default output from pydantic by calling `to_dict()` of ami_families_notice
        if self.ami_families_notice:
            _dict['amiFamiliesNotice'] = self.ami_families_notice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in channel_versions (dict)
        _field_dict = {}
        if self.channel_versions:
            for _key_channel_versions in self.channel_versions:
                if self.channel_versions[_key_channel_versions]:
                    _field_dict[_key_channel_versions] = self.channel_versions[_key_channel_versions].to_dict()
            _dict['channelVersions'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in upgrade_paths (list)
        _items = []
        if self.upgrade_paths:
            for _item_upgrade_paths in self.upgrade_paths:
                if _item_upgrade_paths:
                    _items.append(_item_upgrade_paths.to_dict())
            _dict['upgradePaths'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupportedK8sVersionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amiFamilies": [AMIFamiliesForVersion.from_dict(_item) for _item in obj["amiFamilies"]] if obj.get("amiFamilies") is not None else None,
            "amiFamiliesNotice": Notice.from_dict(obj["amiFamiliesNotice"]) if obj.get("amiFamiliesNotice") is not None else None,
            "channelVersions": dict(
                (_k, ChannelVersions.from_dict(_v))
                for _k, _v in obj["channelVersions"].items()
            )
            if obj.get("channelVersions") is not None
            else None,
            "defaultVersion": obj.get("defaultVersion"),
            "defaultVersionReason": obj.get("defaultVersionReason"),
            "error": Failure.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "limitedBy": obj.get("limitedBy"),
            "minimumVersion": obj.get("minimumVersion"),
            "supportedVersions": obj.get("supportedVersions"),
            "upgradePaths": [K8sUpgradePath.from_dict(_item) for _item in obj["upgradePaths"]] if obj.get("upgradePaths") is not None else None
        })
        return _obj


