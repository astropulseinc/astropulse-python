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
from astropulse._generated.models.account_setup import AccountSetup
from astropulse._generated.models.provisioner_type import ProvisionerType
from astropulse._generated.models.setting_options import SettingOptions
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProvisionerInfo(BaseModel):
    """
    ProvisionerInfo
    """ # noqa: E501
    accelerator_min_kubernetes_version: Optional[StrictStr] = Field(default=None, description="The lowest Kubernetes version (major.minor) a cluster with an accelerator node group may run; set when AcceleratorNodeGroups is true.", alias="acceleratorMinKubernetesVersion", json_schema_extra={"examples": ["1.36"]})
    accelerator_node_groups: Optional[StrictBool] = Field(default=None, description="True when a node group may carry an accelerator (a GPU) on this provisioner.", alias="acceleratorNodeGroups")
    account_setup: Optional[AccountSetup] = Field(default=None, description="Names that setup when NeedsAccountSetup is true.", alias="accountSetup")
    creates_clusters: Optional[StrictBool] = Field(default=None, description="False for a provisioner that joins a cluster you already run instead of creating one.", alias="createsClusters")
    display_name: Optional[StrictStr] = Field(default=None, description="The provisioner's name for people.", alias="displayName")
    docs_path: Optional[StrictStr] = Field(default=None, description="The documentation page for the provisioner, relative to the site root.", alias="docsPath")
    needs_account_setup: Optional[StrictBool] = Field(default=None, description="True when the account needs a one-time setup before the first cluster.", alias="needsAccountSetup")
    settings: Optional[List[SettingOptions]] = Field(default=None, description="The cluster and node group fields this provisioner offers, each with the values or the form of value it accepts; absent when the provisioner does not create clusters.")
    summary: Optional[StrictStr] = Field(default=None, description="Says in one line who runs the control plane and what you manage.")
    type: Optional[ProvisionerType] = Field(default=None, description="The value for provisioner.type in a cluster spec.")
    __properties: ClassVar[List[str]] = ["acceleratorMinKubernetesVersion", "acceleratorNodeGroups", "accountSetup", "createsClusters", "displayName", "docsPath", "needsAccountSetup", "settings", "summary", "type"]

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
        """Create an instance of ProvisionerInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in settings (list)
        _items = []
        if self.settings:
            for _item_settings in self.settings:
                if _item_settings:
                    _items.append(_item_settings.to_dict())
            _dict['settings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProvisionerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "acceleratorMinKubernetesVersion": obj.get("acceleratorMinKubernetesVersion"),
            "acceleratorNodeGroups": obj.get("acceleratorNodeGroups"),
            "accountSetup": obj.get("accountSetup"),
            "createsClusters": obj.get("createsClusters"),
            "displayName": obj.get("displayName"),
            "docsPath": obj.get("docsPath"),
            "needsAccountSetup": obj.get("needsAccountSetup"),
            "settings": [SettingOptions.from_dict(_item) for _item in obj["settings"]] if obj.get("settings") is not None else None,
            "summary": obj.get("summary"),
            "type": obj.get("type")
        })
        return _obj


