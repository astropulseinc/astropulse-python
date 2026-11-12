# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.control_plane_node import ControlPlaneNode
from astropulse._generated.models.cpu_architecture import CPUArchitecture
from astropulse._generated.models.data_plane import DataPlane
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class K8sClusterSpec(BaseModel):
    """
    K8sClusterSpec
    """ # noqa: E501
    architecture: Optional[CPUArchitecture] = Field(default=None, description="The CPU architecture this cluster runs. Usually there is nothing to write here — the platform derives it from the machine types the node groups pin, since every provider picks the node image from the instance type, so pinning m7g.large (or a c4a-* on GCP, a Dpls_v6 on Azure) is already asking for arm64. Declare it when nothing is pinned to derive from: an accelerator-only node group whose machine AstroPulse resolves, or provider-managed compute (EKS Auto Mode, GKE Autopilot). When declared alongside pinned machine types it is checked against them, and a contradiction is refused. Immutable after create.")
    control_plane: Optional[ControlPlaneNode] = Field(default=None, description="The configuration for the control plane", alias="controlPlane")
    data_plane: Optional[DataPlane] = Field(default=None, description="The configuration for the data plane. It is required for normal clusters and must be omitted when the provider owns worker compute: EKS Auto Mode (provisioner.eks.computeMode = `AutoMode`) or GKE Autopilot (provisioner.gke.autopilot = true).", alias="dataPlane")
    __properties: ClassVar[List[str]] = ["architecture", "controlPlane", "dataPlane"]

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
        """Create an instance of K8sClusterSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of control_plane
        if self.control_plane:
            _dict['controlPlane'] = self.control_plane.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_plane
        if self.data_plane:
            _dict['dataPlane'] = self.data_plane.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of K8sClusterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "architecture": obj.get("architecture"),
            "controlPlane": ControlPlaneNode.from_dict(obj["controlPlane"]) if obj.get("controlPlane") is not None else None,
            "dataPlane": DataPlane.from_dict(obj["dataPlane"]) if obj.get("dataPlane") is not None else None
        })
        return _obj


