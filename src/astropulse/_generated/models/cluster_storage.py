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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_storage_binding import ClusterStorageBinding
from astropulse._generated.models.cluster_storage_class import ClusterStorageClass
from astropulse._generated.models.setting_options import SettingOptions
from astropulse._generated.models.storage_observer import StorageObserver
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterStorage(BaseModel):
    """
    ClusterStorage
    """ # noqa: E501
    bindings: Optional[List[ClusterStorageBinding]] = Field(default=None, description="The names applications and add-ons use for storage.")
    classes: Optional[List[ClusterStorageClass]] = Field(default=None, description="The StorageClasses observed on the cluster. Read-only.")
    kind_options: Optional[SettingOptions] = Field(default=None, description="The storage kinds a binding can declare: Shared, Dedicated or Node.", alias="kindOptions")
    observed_at: Optional[datetime] = Field(default=None, description="When the classes were last observed, RFC 3339. Absent when the cluster's storage has not been observed yet, which is not the same as a cluster with no storage classes.", alias="observedAt")
    observed_by: Optional[StorageObserver] = Field(default=None, description="What read the classes.", alias="observedBy")
    __properties: ClassVar[List[str]] = ["bindings", "classes", "kindOptions", "observedAt", "observedBy"]

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
        """Create an instance of ClusterStorage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bindings (list)
        _items = []
        if self.bindings:
            for _item_bindings in self.bindings:
                if _item_bindings:
                    _items.append(_item_bindings.to_dict())
            _dict['bindings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in classes (list)
        _items = []
        if self.classes:
            for _item_classes in self.classes:
                if _item_classes:
                    _items.append(_item_classes.to_dict())
            _dict['classes'] = _items
        # override the default output from pydantic by calling `to_dict()` of kind_options
        if self.kind_options:
            _dict['kindOptions'] = self.kind_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterStorage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bindings": [ClusterStorageBinding.from_dict(_item) for _item in obj["bindings"]] if obj.get("bindings") is not None else None,
            "classes": [ClusterStorageClass.from_dict(_item) for _item in obj["classes"]] if obj.get("classes") is not None else None,
            "kindOptions": SettingOptions.from_dict(obj["kindOptions"]) if obj.get("kindOptions") is not None else None,
            "observedAt": obj.get("observedAt"),
            "observedBy": obj.get("observedBy")
        })
        return _obj


