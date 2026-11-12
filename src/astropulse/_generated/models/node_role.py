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
from astropulse._generated.models.node_role_kind import NodeRoleKind
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class NodeRole(BaseModel):
    """
    NodeRole
    """ # noqa: E501
    kind: Optional[NodeRoleKind] = Field(default=None, description="What the nodes are: an EKS managed node group, Karpenter's nodes, GKE nodes or AKS kubelets.")
    label: Optional[StrictStr] = Field(default=None, description="The name to show for the nodes that run as this identity, such as the node group's name.")
    node_group: Optional[StrictStr] = Field(default=None, description="The node group whose nodes run as this identity; empty when the identity is not one node group's.", alias="nodeGroup")
    role_arn: Optional[StrictStr] = Field(default=None, description="The ARN of the IAM role the nodes run as (EKS).", alias="roleArn")
    role_name: Optional[StrictStr] = Field(default=None, description="The identity's name: the IAM role (EKS), the service account's email (GKE) or the managed identity (AKS).", alias="roleName")
    __properties: ClassVar[List[str]] = ["kind", "label", "nodeGroup", "roleArn", "roleName"]

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
        """Create an instance of NodeRole from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kind": obj.get("kind"),
            "label": obj.get("label"),
            "nodeGroup": obj.get("nodeGroup"),
            "roleArn": obj.get("roleArn"),
            "roleName": obj.get("roleName")
        })
        return _obj


