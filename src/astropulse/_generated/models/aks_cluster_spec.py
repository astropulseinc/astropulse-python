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
from astropulse._generated.models.aks_auto_upgrade_channel import AKSAutoUpgradeChannel
from astropulse._generated.models.aks_network_plugin import AKSNetworkPlugin
from astropulse._generated.models.aks_network_plugin_mode import AKSNetworkPluginMode
from astropulse._generated.models.aks_node_os_upgrade_channel import AKSNodeOSUpgradeChannel
from astropulse._generated.models.credentials import Credentials
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AKSClusterSpec(BaseModel):
    """
    AKSClusterSpec
    """ # noqa: E501
    acr_resource_ids: Optional[Annotated[List[StrictStr], Field(max_length=20)]] = Field(default=None, description="Azure Container Registries the cluster pulls from with no credential (optional, max 20); its kubelet identity gets AcrPull on each, so the connection must be able to assign roles there. Format: /subscriptions/{id}/resourceGroups/{rg}/providers/Microsoft.ContainerRegistry/registries/{name}", alias="acrResourceIds")
    authorized_ip_ranges: Optional[Annotated[List[StrictStr], Field(max_length=200)]] = Field(default=None, description="CIDR blocks that restrict API server access (optional, max 200 entries). Each entry must be a valid CIDR block. Not supported for private clusters.", alias="authorizedIPRanges")
    auto_upgrade_channel: Optional[AKSAutoUpgradeChannel] = Field(default=None, description="How the cluster upgrades its Kubernetes version. When both channels are omitted, AstroPulse sets this to `Stable` and `nodeOsUpgradeChannel` to `NodeImage`; when only this one is omitted, AKS's own default applies.", alias="autoUpgradeChannel")
    credentials: Optional[Credentials] = Field(default=None, description="The Azure credentials the cluster is created and managed with; required for a new cluster. Applying an existing cluster again without them, or with the type and no data, keeps the stored ones.")
    enable_oidc_issuer: Optional[StrictBool] = Field(default=None, description="Enables the OIDC issuer on the cluster (optional, default: true when workload identity is enabled)", alias="enableOidcIssuer")
    enable_workload_identity: Optional[StrictBool] = Field(default=None, description="Enables workload identity federation for pod authentication to Azure services (optional, default: true)", alias="enableWorkloadIdentity")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="The Kubernetes version to create the cluster at (optional): \"1.30\" or \"1.30.14\". \"1.30\" selects the newest supported patch of that minor; if omitted, the default version is used.", alias="kubernetesVersion")
    network_plugin: Optional[AKSNetworkPlugin] = Field(default=None, description="The network plugin the cluster's pods get their addresses from. Defaults to `Azure`.", alias="networkPlugin")
    network_plugin_mode: Optional[AKSNetworkPluginMode] = Field(default=None, description="How the Azure CNI plugin assigns pod addresses. Defaults to `Overlay` when networkPlugin is `Azure`.", alias="networkPluginMode")
    node_os_upgrade_channel: Optional[AKSNodeOSUpgradeChannel] = Field(default=None, description="How the cluster updates its nodes' operating system. When both channels are omitted, AstroPulse sets this to `NodeImage` and `autoUpgradeChannel` to `Stable`; when only this one is omitted, AKS's own default applies.", alias="nodeOsUpgradeChannel")
    private_cluster: Optional[StrictBool] = Field(default=None, description="Enables private API access (optional, default: false). Currently unsupported for managed AKS provisioning.", alias="privateCluster")
    resource_group: StrictStr = Field(description="The Azure resource group name (required). Format: 1-90 characters, alphanumeric, underscores, hyphens, and periods.", alias="resourceGroup")
    subscription_id: StrictStr = Field(description="The Azure subscription ID (required, UUID format)", alias="subscriptionId")
    tags: Optional[Dict[str, StrictStr]] = Field(default=None, description="Azure tags applied to the cluster (optional, at most 47). Names are 1-512 characters without < > % & \\ ? or /; values are at most 256 characters.")
    vnet_subnet_id: Optional[StrictStr] = Field(default=None, description="The full Azure subnet resource ID for BYOVPC (optional). Format: /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vnet}/subnets/{subnet}", alias="vnetSubnetId")
    __properties: ClassVar[List[str]] = ["acrResourceIds", "authorizedIPRanges", "autoUpgradeChannel", "credentials", "enableOidcIssuer", "enableWorkloadIdentity", "kubernetesVersion", "networkPlugin", "networkPluginMode", "nodeOsUpgradeChannel", "privateCluster", "resourceGroup", "subscriptionId", "tags", "vnetSubnetId"]

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
        """Create an instance of AKSClusterSpec from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AKSClusterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "acrResourceIds": obj.get("acrResourceIds"),
            "authorizedIPRanges": obj.get("authorizedIPRanges"),
            "autoUpgradeChannel": obj.get("autoUpgradeChannel"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "enableOidcIssuer": obj.get("enableOidcIssuer"),
            "enableWorkloadIdentity": obj.get("enableWorkloadIdentity"),
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "networkPlugin": obj.get("networkPlugin"),
            "networkPluginMode": obj.get("networkPluginMode"),
            "nodeOsUpgradeChannel": obj.get("nodeOsUpgradeChannel"),
            "privateCluster": obj.get("privateCluster"),
            "resourceGroup": obj.get("resourceGroup"),
            "subscriptionId": obj.get("subscriptionId"),
            "tags": obj.get("tags"),
            "vnetSubnetId": obj.get("vnetSubnetId")
        })
        return _obj


