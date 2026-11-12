# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.accelerator_attachment import AcceleratorAttachment
from astropulse._generated.models.instance_type import InstanceType
from astropulse._generated.models.tainted import Tainted
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpdateNodeGroup(BaseModel):
    """
    UpdateNodeGroup
    """ # noqa: E501
    accelerator: Optional[AcceleratorAttachment] = Field(default=None, description="Optional for update patches, with patch semantics distinct from a plain optional field. Omit it to leave the stored accelerator unchanged. Send an empty message ({}) to clear it — a material change that recreates the node group, which must then carry machineTypes. Send a populated union member to replace it, which also recreates the group.")
    availability_zones: Optional[List[StrictStr]] = Field(default=None, description="Optional for update patches. When omitted, the server preserves the existing value.", alias="availabilityZones")
    disk_size_gb: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The desired root disk for the group's nodes, in whole gigabytes. Omitted, the group keeps the size it has; changing it replaces the group's nodes, and is refused on gke.", alias="diskSizeGB")
    instance_type: Optional[InstanceType] = Field(default=None, description="Optional for update patches. When omitted, the server preserves the existing value.", alias="instanceType")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="The group's Kubernetes node labels (optional); omitted, the group keeps its labels. Keys are Kubernetes label keys, not under kubernetes.io or k8s.io (at most 63 characters in all on eks); values are 1-63 letters, digits, '-', '_' and '.', starting and ending with a letter or digit.")
    machine_types: Optional[List[StrictStr]] = Field(default=None, description="Optional for update patches. When omitted, the server preserves the existing value.", alias="machineTypes")
    max_node: Optional[StrictInt] = Field(default=None, description="The desired maximum node count for the node group. Nil means \"leave as it is\" — see MinNode.", alias="maxNode")
    min_node: Optional[StrictInt] = Field(default=None, description="The desired minimum node count for the node group.  A pointer so that an omitted field stays distinguishable from an explicit zero: since a group may legitimately have a floor of zero, decoding an absent minNode to 0 would turn every partial patch into a scale-to-zero request. Nil means \"leave as it is\" and is filled in from the stored cluster by mergeNodeGroupDefaults.", alias="minNode")
    name: StrictStr = Field(description="The existing node group name to update.")
    taints: Optional[List[Tainted]] = Field(default=None, description="Optional taints to apply.")
    __properties: ClassVar[List[str]] = ["accelerator", "availabilityZones", "diskSizeGB", "instanceType", "labels", "machineTypes", "maxNode", "minNode", "name", "taints"]

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
        """Create an instance of UpdateNodeGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accelerator
        if self.accelerator:
            _dict['accelerator'] = self.accelerator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in taints (list)
        _items = []
        if self.taints:
            for _item_taints in self.taints:
                if _item_taints:
                    _items.append(_item_taints.to_dict())
            _dict['taints'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateNodeGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": AcceleratorAttachment.from_dict(obj["accelerator"]) if obj.get("accelerator") is not None else None,
            "availabilityZones": obj.get("availabilityZones"),
            "diskSizeGB": obj.get("diskSizeGB"),
            "instanceType": obj.get("instanceType"),
            "labels": obj.get("labels"),
            "machineTypes": obj.get("machineTypes"),
            "maxNode": obj.get("maxNode"),
            "minNode": obj.get("minNode"),
            "name": obj.get("name"),
            "taints": [Tainted.from_dict(_item) for _item in obj["taints"]] if obj.get("taints") is not None else None
        })
        return _obj


