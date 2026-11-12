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
from astropulse._generated.models.cluster_addon_apply_options import ClusterAddonApplyOptions
from astropulse._generated.models.cluster_addon_configuration import ClusterAddonConfiguration
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class K8sClusterAddonManifestSpec(BaseModel):
    """
    K8sClusterAddonManifestSpec
    """ # noqa: E501
    cluster_name: Optional[StrictStr] = Field(default=None, description="The name of the cluster the add-on runs on.", alias="clusterName")
    configuration: Optional[ClusterAddonConfiguration] = Field(default=None, description="The add-on's settings. Omitted keeps the installed settings, or takes the add-on's defaults on a new install.")
    options: Optional[ClusterAddonApplyOptions] = Field(default=None, description="How the apply runs. Absent from an add-on spec read.")
    version: Optional[StrictStr] = Field(default=None, description="The add-on version to run. Omitted installs the default version, or keeps the installed one.")
    __properties: ClassVar[List[str]] = ["clusterName", "configuration", "options", "version"]

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
        """Create an instance of K8sClusterAddonManifestSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of K8sClusterAddonManifestSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "configuration": ClusterAddonConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "options": ClusterAddonApplyOptions.from_dict(obj["options"]) if obj.get("options") is not None else None,
            "version": obj.get("version")
        })
        return _obj


