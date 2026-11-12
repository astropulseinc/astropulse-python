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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ControlPlaneNodeGroup(BaseModel):
    """
    ControlPlaneNodeGroup
    """ # noqa: E501
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Kubernetes labels applied to control plane nodes (optional). Keys are Kubernetes label keys, not under kubernetes.io or k8s.io; values are 1-63 letters, digits, '-', '_' and '.', starting and ending with a letter or digit.")
    machine_types: List[StrictStr] = Field(description="The list of machine types for control plane nodes (required, minimum 1 item). Provider-specific formats: eks (e.g. \"t3.medium\"), gke (e.g. \"n1-standard-1\"), aks (e.g. \"Standard_D2s_v3\").", alias="machineTypes")
    max_node: Optional[StrictInt] = Field(default=None, description="The maximum number of control plane nodes (optional, default: 1). Should be an odd number (1, 3, 5) for quorum. Must be >= MinNode.", alias="maxNode")
    min_node: Optional[StrictInt] = Field(default=None, description="The minimum number of control plane nodes (optional, default: 1). Should be an odd number (1, 3, 5) for quorum. Nodes are distributed across availability zones.", alias="minNode")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The control plane node group name (required, 1-50 characters, valid DNS name)")
    __properties: ClassVar[List[str]] = ["labels", "machineTypes", "maxNode", "minNode", "name"]

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
        """Create an instance of ControlPlaneNodeGroup from a JSON string"""
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
        """Create an instance of ControlPlaneNodeGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "labels": obj.get("labels"),
            "machineTypes": obj.get("machineTypes"),
            "maxNode": obj.get("maxNode"),
            "minNode": obj.get("minNode"),
            "name": obj.get("name")
        })
        return _obj


