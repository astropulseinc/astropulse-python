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
from typing_extensions import Annotated
from astropulse._generated.models.credentials import Credentials
from astropulse._generated.models.gke_release_channel import GKEReleaseChannel
from astropulse._generated.models.gke_subnet_config import GKESubnetConfig
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GKEClusterSpec(BaseModel):
    """
    GKEClusterSpec
    """ # noqa: E501
    authorized_networks: Optional[Annotated[List[StrictStr], Field(max_length=50)]] = Field(default=None, description="CIDR blocks allowed to access the Kubernetes API server (optional, max 50 entries). Each entry must be a valid CIDR block (e.g. \"10.0.0.0/8\", \"203.0.113.5/32\"). If omitted, API access is unrestricted (not recommended for production).", alias="authorizedNetworks")
    autopilot: Optional[StrictBool] = Field(default=None, description="Enables GKE Autopilot mode where Google manages nodes, scaling, and security (optional, default: false). When disabled, uses Standard GKE with traditional node management.")
    credentials: Optional[Credentials] = Field(default=None, description="The GCP credentials the cluster is created and managed with; required for a new cluster. Applying an existing cluster again without them, or with the type and no data, keeps the stored ones.")
    enable_workload_identity: Optional[StrictBool] = Field(default=None, description="Enables Workload Identity for secure pod-to-GCP service authentication (optional, default: true). When enabled, pods can securely access GCP services using IAM without service account keys.", alias="enableWorkloadIdentity")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="The Kubernetes version to create the cluster at (optional): \"1.30\", \"1.30.14\" or a full GKE version such as \"1.30.14-gke.1096000\". A shorter form selects the newest matching version the release channel offers; if omitted, the channel's default version is used.", alias="kubernetesVersion")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Google Cloud labels applied to the cluster (optional, at most 64). Keys are 1-63 and values at most 63 lowercase letters, digits, '_' and '-'; keys start with a lowercase letter.")
    master_ipv4_cidr_block: Optional[StrictStr] = Field(default=None, description="The IP range for the GKE control plane of a private cluster (optional, default: \"172.16.0.0/28\"). Must be exactly /28 CIDR in RFC 1918 private range (10.x, 172.16-31.x, 192.168.x). Change only if the default conflicts with your network. Examples: \"172.16.0.0/28\", \"10.0.0.0/28\", \"192.168.0.0/28\"", alias="masterIPv4CidrBlock")
    network_cidr: Optional[StrictStr] = Field(default=None, description="The node IP range of the subnet created for the cluster, for example \"10.50.0.0/20\"; it is allowed only when networkId is omitted (optional; if omitted, a free range is chosen). It must be a /8 to /29 block inside 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 or 100.64.0.0/10 that no other subnet in the network uses.", alias="networkCIDR")
    network_id: Optional[StrictStr] = Field(default=None, description="The existing GCP VPC network name (optional). Format: 1-63 lowercase letters, digits, or hyphens. If omitted, the cluster joins the project's default network on a subnet created for it.", alias="networkId")
    private_cluster: Optional[StrictBool] = Field(default=None, description="Gives the nodes internal IPs only (optional, default: false; requires credentials.type `Dynamic`). The Kubernetes API server keeps its public endpoint: restrict it with authorizedNetworks. On the default network (no networkId) AstroPulse adds a Cloud NAT for the nodes' egress; on your own network (networkId), the subnet must already have one.", alias="privateCluster")
    project_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The GCP project ID (required). Format: 6-30 lowercase letters, digits, or hyphens; must start with a letter. Example: \"my-gcp-project\"", alias="projectId")
    release_channel: Optional[GKEReleaseChannel] = Field(default=None, description="The release channel the cluster takes its Kubernetes versions from. Defaults to `Stable`.", alias="releaseChannel")
    subnet: Optional[GKESubnetConfig] = Field(default=None, description="The regional subnet configuration for BYOVPC (required when NetworkId is provided). GKE uses regional subnets with secondary IP ranges for pods and services.")
    __properties: ClassVar[List[str]] = ["authorizedNetworks", "autopilot", "credentials", "enableWorkloadIdentity", "kubernetesVersion", "labels", "masterIPv4CidrBlock", "networkCIDR", "networkId", "privateCluster", "projectId", "releaseChannel", "subnet"]

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
        """Create an instance of GKEClusterSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subnet
        if self.subnet:
            _dict['subnet'] = self.subnet.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GKEClusterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorizedNetworks": obj.get("authorizedNetworks"),
            "autopilot": obj.get("autopilot"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "enableWorkloadIdentity": obj.get("enableWorkloadIdentity"),
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "labels": obj.get("labels"),
            "masterIPv4CidrBlock": obj.get("masterIPv4CidrBlock"),
            "networkCIDR": obj.get("networkCIDR"),
            "networkId": obj.get("networkId"),
            "privateCluster": obj.get("privateCluster"),
            "projectId": obj.get("projectId"),
            "releaseChannel": obj.get("releaseChannel"),
            "subnet": GKESubnetConfig.from_dict(obj["subnet"]) if obj.get("subnet") is not None else None
        })
        return _obj


