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
from astropulse._generated.models.aks_update_spec import AKSUpdateSpec
from astropulse._generated.models.eks_update_spec import EKSUpdateSpec
from astropulse._generated.models.gke_update_spec import GKEUpdateSpec
from astropulse._generated.models.self_hosted_update_spec import SelfHostedUpdateSpec
from astropulse._generated.models.update_config import UpdateConfig
from astropulse._generated.models.update_node_group import UpdateNodeGroup
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpdateClusterSpec(BaseModel):
    """
    UpdateClusterSpec
    """ # noqa: E501
    aks: Optional[AKSUpdateSpec] = Field(default=None, description="The specification for aks-specific updates (optional, for aks clusters only)")
    eks: Optional[EKSUpdateSpec] = Field(default=None, description="Provider-specific update configurations (optional, at most one should be set matching your cluster's provisioner) EKS is the specification for eks-specific updates (optional, for eks clusters only)")
    gke: Optional[GKEUpdateSpec] = Field(default=None, description="The specification for gke-specific updates (optional, for gke clusters only)")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="The target Kubernetes version (optional). For upgrade: must be at most 1 minor version above current. For rollback: set allowDowngrade=true in updateConfig.", alias="kubernetesVersion")
    node_groups: Optional[List[UpdateNodeGroup]] = Field(default=None, description="Specifies node groups to update (optional). Each entry patches an existing node group by name. Omitted fields are merged from the stored cluster definition — no need to repeat unchanged values.", alias="nodeGroups")
    remove_node_groups: Optional[List[StrictStr]] = Field(default=None, description="Names the node groups to remove from the cluster (optional). Each group's nodes are drained, then the group is deleted.", alias="removeNodeGroups")
    self_hosted: Optional[SelfHostedUpdateSpec] = Field(default=None, description="The specification for selfHosted cluster updates (optional, for selfHosted clusters only)", alias="selfHosted")
    tags: Optional[Dict[str, StrictStr]] = Field(default=None, description="Replace the cluster's cloud tags (labels on GKE) with this set, following its provider's create rule; omitted keeps them and an empty map removes them. Tags AstroPulse and the cloud write are kept, and self-hosted clusters take none.")
    update_config: Optional[UpdateConfig] = Field(default=None, description="Provides safety and rollback controls for the update operation (optional).", alias="updateConfig")
    __properties: ClassVar[List[str]] = ["aks", "eks", "gke", "kubernetesVersion", "nodeGroups", "removeNodeGroups", "selfHosted", "tags", "updateConfig"]

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
        """Create an instance of UpdateClusterSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aks
        if self.aks:
            _dict['aks'] = self.aks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eks
        if self.eks:
            _dict['eks'] = self.eks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gke
        if self.gke:
            _dict['gke'] = self.gke.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in node_groups (list)
        _items = []
        if self.node_groups:
            for _item_node_groups in self.node_groups:
                if _item_node_groups:
                    _items.append(_item_node_groups.to_dict())
            _dict['nodeGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of self_hosted
        if self.self_hosted:
            _dict['selfHosted'] = self.self_hosted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of update_config
        if self.update_config:
            _dict['updateConfig'] = self.update_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateClusterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aks": AKSUpdateSpec.from_dict(obj["aks"]) if obj.get("aks") is not None else None,
            "eks": EKSUpdateSpec.from_dict(obj["eks"]) if obj.get("eks") is not None else None,
            "gke": GKEUpdateSpec.from_dict(obj["gke"]) if obj.get("gke") is not None else None,
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "nodeGroups": [UpdateNodeGroup.from_dict(_item) for _item in obj["nodeGroups"]] if obj.get("nodeGroups") is not None else None,
            "removeNodeGroups": obj.get("removeNodeGroups"),
            "selfHosted": SelfHostedUpdateSpec.from_dict(obj["selfHosted"]) if obj.get("selfHosted") is not None else None,
            "tags": obj.get("tags"),
            "updateConfig": UpdateConfig.from_dict(obj["updateConfig"]) if obj.get("updateConfig") is not None else None
        })
        return _obj


