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
from astropulse._generated.models.cluster_storage_binding_use import ClusterStorageBindingUse
from astropulse._generated.models.storage_binding_state import StorageBindingState
from astropulse._generated.models.storage_kind import StorageKind
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterStorageBinding(BaseModel):
    """
    ClusterStorageBinding
    """ # noqa: E501
    var_class: StrictStr = Field(description="The StorageClass the name refers to. It must be one the cluster has.", alias="class")
    kind: Optional[StorageKind] = Field(default=None, description="What the storage provides. Required when AstroPulse does not recognize the class's driver; otherwise it is filled in and cannot disagree with what the driver provides.")
    name: StrictStr = Field(description="The name to use for this storage. A lowercase DNS label.")
    state: Optional[StorageBindingState] = Field(default=None, description="Whether the class is on the cluster. Read-only.")
    used_by: Optional[List[ClusterStorageBindingUse]] = Field(default=None, description="The installed add-on settings that ask for this name. A name in use cannot be unbound or pointed at another class. Read-only.", alias="usedBy")
    __properties: ClassVar[List[str]] = ["class", "kind", "name", "state", "usedBy"]

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
        """Create an instance of ClusterStorageBinding from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in used_by (list)
        _items = []
        if self.used_by:
            for _item_used_by in self.used_by:
                if _item_used_by:
                    _items.append(_item_used_by.to_dict())
            _dict['usedBy'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterStorageBinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "class": obj.get("class"),
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "state": obj.get("state"),
            "usedBy": [ClusterStorageBindingUse.from_dict(_item) for _item in obj["usedBy"]] if obj.get("usedBy") is not None else None
        })
        return _obj


