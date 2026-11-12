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
from astropulse._generated.models.addon_cloud_access import AddonCloudAccess
from astropulse._generated.models.addon_configuration_field import AddonConfigurationField
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonCatalogEntry(BaseModel):
    """
    ClusterAddonCatalogEntry
    """ # noqa: E501
    category: Optional[StrictStr] = Field(default=None, description="Groups the add-on in a catalog listing.")
    cloud_access: Optional[AddonCloudAccess] = Field(default=None, description="How the add-on reaches a cloud account of yours: the account your identity must trust, and the key credentials take in a Secret. Absent for an add-on that reaches none.", alias="cloudAccess")
    cluster_managed: Optional[StrictBool] = Field(default=None, description="Marks an add-on installed and removed with the cluster, which cannot be deleted on its own.", alias="clusterManaged")
    compatible: Optional[StrictBool] = Field(default=None, description="Reports whether the add-on can be deployed on the cluster asked about.")
    configuration: Optional[List[AddonConfigurationField]] = Field(default=None, description="What this add-on accepts, flattened to dotted paths. Derived from the REST types themselves, so it cannot describe a setting the API would refuse or omit one it accepts. Empty for an add-on that takes no configuration.")
    configuration_property: Optional[StrictStr] = Field(default=None, description="The JSON property this add-on's configuration is written under, empty for one that takes none. Published because it is not derivable from the add-on's name -- workload-autoscaling is written workloadAutoscaling -- and a client building the payload from Configuration below needs the key to nest it under.", alias="configurationProperty")
    dependencies: Optional[List[StrictStr]] = Field(default=None, description="The public names of add-ons this one needs installed.")
    description: Optional[StrictStr] = Field(default=None, description="Says what installing it gives the cluster.")
    display_name: Optional[StrictStr] = Field(default=None, description="The add-on's name in front of a person.", alias="displayName")
    docs_url: Optional[StrictStr] = Field(default=None, description="Where this add-on is documented, as a path relative to the documentation site.", alias="docsUrl")
    incompatibility_reason: Optional[StrictStr] = Field(default=None, description="Says why it cannot be installed now: what rules it out when Compatible is false, or why no installable version is listed.", alias="incompatibilityReason")
    installable_versions: Optional[List[StrictStr]] = Field(default=None, description="The versions of this add-on that can be installed on this cluster, oldest first. Empty when none can.", alias="installableVersions")
    shared_configuration: Optional[List[AddonConfigurationField]] = Field(default=None, description="What every add-on accepts, flattened to dotted paths and written directly under configuration, beside the add-on's own block.", alias="sharedConfiguration")
    type: Optional[ClusterAddonType] = Field(default=None, description="The add-on's public name, and what every add-on command takes.")
    unlocks: Optional[List[StrictStr]] = Field(default=None, description="Says what installing this add-on makes usable, such as \"model scaling on queue depth\".")
    __properties: ClassVar[List[str]] = ["category", "cloudAccess", "clusterManaged", "compatible", "configuration", "configurationProperty", "dependencies", "description", "displayName", "docsUrl", "incompatibilityReason", "installableVersions", "sharedConfiguration", "type", "unlocks"]

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
        """Create an instance of ClusterAddonCatalogEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cloud_access
        if self.cloud_access:
            _dict['cloudAccess'] = self.cloud_access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in configuration (list)
        _items = []
        if self.configuration:
            for _item_configuration in self.configuration:
                if _item_configuration:
                    _items.append(_item_configuration.to_dict())
            _dict['configuration'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shared_configuration (list)
        _items = []
        if self.shared_configuration:
            for _item_shared_configuration in self.shared_configuration:
                if _item_shared_configuration:
                    _items.append(_item_shared_configuration.to_dict())
            _dict['sharedConfiguration'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonCatalogEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "cloudAccess": AddonCloudAccess.from_dict(obj["cloudAccess"]) if obj.get("cloudAccess") is not None else None,
            "clusterManaged": obj.get("clusterManaged"),
            "compatible": obj.get("compatible"),
            "configuration": [AddonConfigurationField.from_dict(_item) for _item in obj["configuration"]] if obj.get("configuration") is not None else None,
            "configurationProperty": obj.get("configurationProperty"),
            "dependencies": obj.get("dependencies"),
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "docsUrl": obj.get("docsUrl"),
            "incompatibilityReason": obj.get("incompatibilityReason"),
            "installableVersions": obj.get("installableVersions"),
            "sharedConfiguration": [AddonConfigurationField.from_dict(_item) for _item in obj["sharedConfiguration"]] if obj.get("sharedConfiguration") is not None else None,
            "type": obj.get("type"),
            "unlocks": obj.get("unlocks")
        })
        return _obj


