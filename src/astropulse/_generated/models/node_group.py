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
from astropulse._generated.models.capacity_block_status import CapacityBlockStatus
from astropulse._generated.models.instance_type import InstanceType
from astropulse._generated.models.node_group_removal import NodeGroupRemoval
from astropulse._generated.models.node_group_state import NodeGroupState
from astropulse._generated.models.tainted import Tainted
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class NodeGroup(BaseModel):
    """
    NodeGroup
    """ # noqa: E501
    accelerator: Optional[AcceleratorAttachment] = Field(default=None, description="Requests accelerator hardware for this node group (optional). Exactly one member of the union must be set; gpu is the supported member. Not available on selfHosted clusters.")
    availability_zones: Optional[List[StrictStr]] = Field(default=None, description="The list of availability zones for this node group (optional). Default behavior: if omitted, the server auto-selects the first 3 sorted zones in the region (or fewer if the region has < 3 zones). For aks, Azure manages zone placement automatically. Constraints:   - Maximum 3 zones per node group.   - Zones must be valid for the cluster's region (validated server-side).   - Zones must be a subset of the cluster/control plane zones (eks, gke).   - Zones are immutable after creation — changing zones requires deleting and recreating the node group. Example for eks: [\"us-west-2a\", \"us-west-2b\"] Example for gke: [\"us-central1-a\", \"us-central1-b\", \"us-central1-c\"]", alias="availabilityZones")
    capacity_block: Optional[CapacityBlockStatus] = Field(default=None, description="The Capacity Block a CapacityBlock node group runs on (read-only; ignored on input).", alias="capacityBlock")
    disk_size_gb: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The root disk of every node in this group, in whole gigabytes (optional). It holds the operating system, the images the node pulls and anything written to the node's local disk, including the model weight cache. Accepted range: 20 to 16384 on eks and selfHosted, 20 to 65536 on gke, 30 to 2048 on aks; omitted, the provider's default applies (100 on eks and gke, 20 on selfHosted, the machine type's own size on aks). Changing it replaces the group's nodes, and is refused on gke.", alias="diskSizeGB")
    instance_type: InstanceType = Field(description="How the node group's nodes are bought; OnDemand when omitted. It cannot change on an existing node group.", alias="instanceType")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Kubernetes labels applied to nodes in this group (optional), such as {\"tier\": \"frontend\", \"team.example.com/owner\": \"ml\"}. Keys are Kubernetes label keys, not under kubernetes.io or k8s.io (at most 63 characters in all on eks); values are 1-63 letters, digits, '-', '_' and '.', starting and ending with a letter or digit.")
    machine_types: Optional[List[StrictStr]] = Field(default=None, description="The list of machine types for nodes. Provider-specific formats: eks (e.g. \"t3.medium\"), gke (e.g. \"n1-standard-1\"), aks (e.g. \"Standard_D2s_v3\"). Required unless Accelerator is set. Supplying only machineTypes keeps explicit machine selection; supplying only accelerator lets AstroPulse resolve compatible machine types; supplying both requires every listed machine to satisfy the accelerator; supplying neither is invalid. Multiple entries are honoured on eks, where the node group may draw from every listed type. gke, aks and selfHosted node groups run a single machine type — supply exactly one there; a longer list is rejected.", alias="machineTypes")
    max_node: StrictInt = Field(description="The maximum number of nodes in the group (required, minimum: 1). Must be >= MinNode. For control plane node groups, must be an odd number.  On gke, aks and selfHosted the provider's autoscaler scales the group between minNode and maxNode. On eks maxNode has no effect: the group runs at minNode, and elastic capacity, GPUs included, comes from the karpenter add-on.", alias="maxNode")
    min_node: Optional[StrictInt] = Field(default=None, description="The minimum number of nodes in the group. Must be <= MaxNode.  Zero means the group holds no nodes while idle and is scaled up when a pod needs one, which is only honoured where an autoscaler watches the group: gke, aks (except its first node group, which becomes the system pool), and selfHosted. It is rejected on eks, where managed node groups are fixed capacity and Karpenter provides elastic capacity instead.  To undo it, set minNode back to 1 or more and apply again — the same update path, no separate operation.", alias="minNode")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The node group name (required, 1-50 characters, valid DNS name). Format: lowercase alphanumeric and hyphens, must start with a letter. Example: \"ng-workers-1\"")
    removal: Optional[NodeGroupRemoval] = Field(default=None, description="Says whether an update can remove this node group now (read-only; ignored on input). Present on worker node groups.")
    state: Optional[NodeGroupState] = Field(default=None, description="Adding while a running update creates the node group, and absent otherwise (read-only; ignored on input).")
    taints: Optional[List[Tainted]] = Field(default=None, description="Kubernetes taints applied to nodes in this group (optional)")
    __properties: ClassVar[List[str]] = ["accelerator", "availabilityZones", "capacityBlock", "diskSizeGB", "instanceType", "labels", "machineTypes", "maxNode", "minNode", "name", "removal", "state", "taints"]

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
        """Create an instance of NodeGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of capacity_block
        if self.capacity_block:
            _dict['capacityBlock'] = self.capacity_block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of removal
        if self.removal:
            _dict['removal'] = self.removal.to_dict()
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
        """Create an instance of NodeGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": AcceleratorAttachment.from_dict(obj["accelerator"]) if obj.get("accelerator") is not None else None,
            "availabilityZones": obj.get("availabilityZones"),
            "capacityBlock": CapacityBlockStatus.from_dict(obj["capacityBlock"]) if obj.get("capacityBlock") is not None else None,
            "diskSizeGB": obj.get("diskSizeGB"),
            "instanceType": obj.get("instanceType"),
            "labels": obj.get("labels"),
            "machineTypes": obj.get("machineTypes"),
            "maxNode": obj.get("maxNode"),
            "minNode": obj.get("minNode"),
            "name": obj.get("name"),
            "removal": NodeGroupRemoval.from_dict(obj["removal"]) if obj.get("removal") is not None else None,
            "state": obj.get("state"),
            "taints": [Tainted.from_dict(_item) for _item in obj["taints"]] if obj.get("taints") is not None else None
        })
        return _obj


