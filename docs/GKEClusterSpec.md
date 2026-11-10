# GKEClusterSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_networks** | **List[str]** | CIDR blocks allowed to access the Kubernetes API server (optional, max 50 entries). Each entry must be a valid CIDR block (e.g. \&quot;10.0.0.0/8\&quot;, \&quot;203.0.113.5/32\&quot;). If omitted, API access is unrestricted (not recommended for production). | [optional] 
**autopilot** | **bool** | Enables GKE Autopilot mode where Google manages nodes, scaling, and security (optional, default: false). When disabled, uses Standard GKE with traditional node management. | [optional] 
**credentials** | [**Credentials**](Credentials.md) | The GCP credentials the cluster is created and managed with; required for a new cluster. Applying an existing cluster again without them, or with the type and no data, keeps the stored ones. | [optional] 
**enable_workload_identity** | **bool** | Enables Workload Identity for secure pod-to-GCP service authentication (optional, default: true). When enabled, pods can securely access GCP services using IAM without service account keys. | [optional] 
**kubernetes_version** | **str** | The Kubernetes version to create the cluster at (optional): \&quot;1.30\&quot;, \&quot;1.30.14\&quot; or a full GKE version such as \&quot;1.30.14-gke.1096000\&quot;. A shorter form selects the newest matching version the release channel offers; if omitted, the channel&#39;s default version is used. | [optional] 
**labels** | **Dict[str, str]** | Google Cloud labels applied to the cluster (optional, at most 64). Keys are 1-63 and values at most 63 lowercase letters, digits, &#39;_&#39; and &#39;-&#39;; keys start with a lowercase letter. | [optional] 
**master_ipv4_cidr_block** | **str** | The IP range for the GKE control plane of a private cluster (optional, default: \&quot;172.16.0.0/28\&quot;). Must be exactly /28 CIDR in RFC 1918 private range (10.x, 172.16-31.x, 192.168.x). Change only if the default conflicts with your network. Examples: \&quot;172.16.0.0/28\&quot;, \&quot;10.0.0.0/28\&quot;, \&quot;192.168.0.0/28\&quot; | [optional] 
**network_cidr** | **str** | The node IP range of the subnet created for the cluster, for example \&quot;10.50.0.0/20\&quot;; it is allowed only when networkId is omitted (optional; if omitted, a free range is chosen). It must be a /8 to /29 block inside 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 or 100.64.0.0/10 that no other subnet in the network uses. | [optional] 
**network_id** | **str** | The existing GCP VPC network name (optional). Format: 1-63 lowercase letters, digits, or hyphens. If omitted, the cluster joins the project&#39;s default network on a subnet created for it. | [optional] 
**private_cluster** | **bool** | Gives the nodes internal IPs only (optional, default: false; requires credentials.type &#x60;Dynamic&#x60;). The Kubernetes API server keeps its public endpoint: restrict it with authorizedNetworks. On the default network (no networkId) AstroPulse adds a Cloud NAT for the nodes&#39; egress; on your own network (networkId), the subnet must already have one. | [optional] 
**project_id** | **str** | The GCP project ID (required). Format: 6-30 lowercase letters, digits, or hyphens; must start with a letter. Example: \&quot;my-gcp-project\&quot; | 
**release_channel** | [**GKEReleaseChannel**](GKEReleaseChannel.md) | The release channel the cluster takes its Kubernetes versions from. Defaults to &#x60;Stable&#x60;. | [optional] 
**subnet** | [**GKESubnetConfig**](GKESubnetConfig.md) | The regional subnet configuration for BYOVPC (required when NetworkId is provided). GKE uses regional subnets with secondary IP ranges for pods and services. | [optional] 

## Example

```python
from astropulse._generated.models.gke_cluster_spec import GKEClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GKEClusterSpec from a JSON string
gke_cluster_spec_instance = GKEClusterSpec.from_json(json)
# print the JSON string representation of the object
print(GKEClusterSpec.to_json())

# convert the object into a dict
gke_cluster_spec_dict = gke_cluster_spec_instance.to_dict()
# create an instance of GKEClusterSpec from a dict
gke_cluster_spec_from_dict = GKEClusterSpec.from_dict(gke_cluster_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


