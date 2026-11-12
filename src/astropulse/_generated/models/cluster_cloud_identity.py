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
from astropulse._generated.models.node_role import NodeRole
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterCloudIdentity(BaseModel):
    """
    ClusterCloudIdentity
    """ # noqa: E501
    kubelet_identity_object_id: Optional[StrictStr] = Field(default=None, description="The object ID of the AKS kubelet identity, which image pulls use.", alias="kubeletIdentityObjectId")
    node_roles: Optional[List[NodeRole]] = Field(default=None, description="The identities the cluster's nodes run as: one per node group on EKS, plus one for Karpenter's nodes; on GKE and AKS one for all nodes, or one per node pool when GKE pools differ.", alias="nodeRoles")
    node_service_account: Optional[StrictStr] = Field(default=None, description="The service account GKE nodes run as.", alias="nodeServiceAccount")
    oidc_issuer_url: Optional[StrictStr] = Field(default=None, description="The cluster's OIDC issuer (EKS, AKS), for workload identity trust.", alias="oidcIssuerUrl")
    workload_identity_pool: Optional[StrictStr] = Field(default=None, description="The GKE workload identity pool, <project>.svc.id.goog.", alias="workloadIdentityPool")
    __properties: ClassVar[List[str]] = ["kubeletIdentityObjectId", "nodeRoles", "nodeServiceAccount", "oidcIssuerUrl", "workloadIdentityPool"]

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
        """Create an instance of ClusterCloudIdentity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in node_roles (list)
        _items = []
        if self.node_roles:
            for _item_node_roles in self.node_roles:
                if _item_node_roles:
                    _items.append(_item_node_roles.to_dict())
            _dict['nodeRoles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterCloudIdentity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kubeletIdentityObjectId": obj.get("kubeletIdentityObjectId"),
            "nodeRoles": [NodeRole.from_dict(_item) for _item in obj["nodeRoles"]] if obj.get("nodeRoles") is not None else None,
            "nodeServiceAccount": obj.get("nodeServiceAccount"),
            "oidcIssuerUrl": obj.get("oidcIssuerUrl"),
            "workloadIdentityPool": obj.get("workloadIdentityPool")
        })
        return _obj


