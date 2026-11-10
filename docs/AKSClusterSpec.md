# AKSClusterSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acr_resource_ids** | **List[str]** | Azure Container Registries the cluster pulls from with no credential (optional, max 20); its kubelet identity gets AcrPull on each, so the connection must be able to assign roles there. Format: /subscriptions/{id}/resourceGroups/{rg}/providers/Microsoft.ContainerRegistry/registries/{name} | [optional] 
**authorized_ip_ranges** | **List[str]** | CIDR blocks that restrict API server access (optional, max 200 entries). Each entry must be a valid CIDR block. Not supported for private clusters. | [optional] 
**auto_upgrade_channel** | [**AKSAutoUpgradeChannel**](AKSAutoUpgradeChannel.md) | How the cluster upgrades its Kubernetes version. When both channels are omitted, AstroPulse sets this to &#x60;Stable&#x60; and &#x60;nodeOsUpgradeChannel&#x60; to &#x60;NodeImage&#x60;; when only this one is omitted, AKS&#39;s own default applies. | [optional] 
**credentials** | [**Credentials**](Credentials.md) | The Azure credentials the cluster is created and managed with; required for a new cluster. Applying an existing cluster again without them, or with the type and no data, keeps the stored ones. | [optional] 
**enable_oidc_issuer** | **bool** | Enables the OIDC issuer on the cluster (optional, default: true when workload identity is enabled) | [optional] 
**enable_workload_identity** | **bool** | Enables workload identity federation for pod authentication to Azure services (optional, default: true) | [optional] 
**kubernetes_version** | **str** | The Kubernetes version to create the cluster at (optional): \&quot;1.30\&quot; or \&quot;1.30.14\&quot;. \&quot;1.30\&quot; selects the newest supported patch of that minor; if omitted, the default version is used. | [optional] 
**network_plugin** | [**AKSNetworkPlugin**](AKSNetworkPlugin.md) | The network plugin the cluster&#39;s pods get their addresses from. Defaults to &#x60;Azure&#x60;. | [optional] 
**network_plugin_mode** | [**AKSNetworkPluginMode**](AKSNetworkPluginMode.md) | How the Azure CNI plugin assigns pod addresses. Defaults to &#x60;Overlay&#x60; when networkPlugin is &#x60;Azure&#x60;. | [optional] 
**node_os_upgrade_channel** | [**AKSNodeOSUpgradeChannel**](AKSNodeOSUpgradeChannel.md) | How the cluster updates its nodes&#39; operating system. When both channels are omitted, AstroPulse sets this to &#x60;NodeImage&#x60; and &#x60;autoUpgradeChannel&#x60; to &#x60;Stable&#x60;; when only this one is omitted, AKS&#39;s own default applies. | [optional] 
**private_cluster** | **bool** | Enables private API access (optional, default: false). Currently unsupported for managed AKS provisioning. | [optional] 
**resource_group** | **str** | The Azure resource group name (required). Format: 1-90 characters, alphanumeric, underscores, hyphens, and periods. | 
**subscription_id** | **str** | The Azure subscription ID (required, UUID format) | 
**tags** | **Dict[str, str]** | Azure tags applied to the cluster (optional, at most 47). Names are 1-512 characters without &lt; &gt; % &amp; \\ ? or /; values are at most 256 characters. | [optional] 
**vnet_subnet_id** | **str** | The full Azure subnet resource ID for BYOVPC (optional). Format: /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vnet}/subnets/{subnet} | [optional] 

## Example

```python
from astropulse._generated.models.aks_cluster_spec import AKSClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AKSClusterSpec from a JSON string
aks_cluster_spec_instance = AKSClusterSpec.from_json(json)
# print the JSON string representation of the object
print(AKSClusterSpec.to_json())

# convert the object into a dict
aks_cluster_spec_dict = aks_cluster_spec_instance.to_dict()
# create an instance of AKSClusterSpec from a dict
aks_cluster_spec_from_dict = AKSClusterSpec.from_dict(aks_cluster_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


