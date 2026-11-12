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
from astropulse._generated.models.cpu_architecture import CPUArchitecture
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class RegisterClusterRequest(BaseModel):
    """
    RegisterClusterRequest
    """ # noqa: E501
    agent_namespace: Optional[StrictStr] = Field(default=None, description="Where the Astro agent is installed. It is persisted so agent-driven add-ons can place their local control ConfigMaps correctly.", alias="agentNamespace")
    agent_update: Optional[StrictBool] = Field(default=None, description="Returns the manifest that upgrades the agent of a cluster that is already registered, keeping its identity. It requires dryRun.", alias="agentUpdate")
    architecture: Optional[CPUArchitecture] = Field(default=None, description="The CPU architecture the cluster's nodes run.")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster name. Set from the URL path param — ignored if provided in body.", alias="clusterName")
    dry_run: Optional[StrictBool] = Field(default=None, description="Generates the agent manifest without persisting the cluster or waiting for agent connection.", alias="dryRun")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="Optional. If omitted, it is detected from the cluster.", alias="kubernetesVersion")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Key/value pairs stored on the cluster, following the Kubernetes label rules. Keys are Kubernetes label keys, not under kubernetes.io or k8s.io; values are 1-63 letters, digits, '-', '_' and '.', starting and ending with a letter or digit.")
    provisioner: Optional[StrictStr] = Field(default=None, description="Set automatically by the server — ignored if provided in the request body.")
    provisioner_config: Optional[Dict[str, StrictStr]] = Field(default=None, description="What is known about the cluster: \"provider\", detected from the kubeconfig, and on EKS \"eksComputeMode\" when it is known.", alias="provisionerConfig")
    region: Optional[StrictStr] = Field(default=None, description="The cloud region or zone the cluster runs in, such as us-east-1, or local for a cluster outside a cloud. Defaults to local.")
    __properties: ClassVar[List[str]] = ["agentNamespace", "agentUpdate", "architecture", "clusterName", "dryRun", "kubernetesVersion", "labels", "provisioner", "provisionerConfig", "region"]

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
        """Create an instance of RegisterClusterRequest from a JSON string"""
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
        """Create an instance of RegisterClusterRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentNamespace": obj.get("agentNamespace"),
            "agentUpdate": obj.get("agentUpdate"),
            "architecture": obj.get("architecture"),
            "clusterName": obj.get("clusterName"),
            "dryRun": obj.get("dryRun"),
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "labels": obj.get("labels"),
            "provisioner": obj.get("provisioner"),
            "provisionerConfig": obj.get("provisionerConfig"),
            "region": obj.get("region")
        })
        return _obj


