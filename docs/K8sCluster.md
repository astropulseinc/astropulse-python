# K8sCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The cloud provider account identifier. For GKE: GCP project ID. For EKS: AWS account ID. For AKS: Azure subscription ID. Used to generate provider-specific cleanup commands after cluster deletion. | [optional] 
**addons** | [**List[ClusterAddonSummary]**](ClusterAddonSummary.md) | Lists the add-ons installed on the cluster, with each one&#39;s version and status. Present on a single-cluster read. | [optional] 
**agent_capabilities** | **List[str]** | The protocol features advertised by the live agent. | [optional] 
**agent_capability_statuses** | [**List[AgentCapabilityStatus]**](AgentCapabilityStatus.md) | The state of each capability of the cluster&#39;s agent (registered clusters only). | [optional] 
**agent_certificate** | [**AgentCertificateStatus**](AgentCertificateStatus.md) | When the AstroPulse agent&#39;s certificate on this cluster expires and whether it needs attention; omitted when not known. | [optional] 
**agent_namespace** | **str** | Where the registered-cluster agent is installed. | [optional] 
**agent_version** | **str** | The version of the agent running on the cluster (registered clusters only). | [optional] 
**application** | [**List[ClusterApplication]**](ClusterApplication.md) | Represents the applications deployed on the cluster | [optional] 
**approval_token** | **str** | A single-use token for approving or rejecting this cluster request. Present only to the organization owner, while the state is ApprovalPending; it is used with the approval API. | [optional] 
**architecture** | [**CPUArchitecture**](CPUArchitecture.md) | The CPU architecture the cluster&#39;s nodes run. | [optional] 
**capacity_label** | **str** | How many worker nodes the cluster&#39;s node groups run, such as \&quot;4 nodes\&quot; or \&quot;up to 10 nodes\&quot;, with \&quot;when ready\&quot; while the cluster is being created. Absent on a registered cluster, one with no node groups, and one that does not exist, such as a failed create or a deleted cluster. | [optional] 
**cloud_identity** | [**ClusterCloudIdentity**](ClusterCloudIdentity.md) | Who the cluster is in its cloud, so you can grant it access on your side (a registry, a bucket, a key). Read from what the platform created; omitted until read. | [optional] 
**cluster_fqdn** | **str** | The fully qualified domain name of the cluster | [optional] 
**cluster_id** | **str** | The unique identifier for the cluster | [optional] 
**cluster_name** | **str** | The name of the cluster | [optional] 
**compute_mode** | [**ClusterComputeMode**](ClusterComputeMode.md) | Who manages this cluster&#39;s worker nodes. Omitted for registered clusters and wherever it is not known. | [optional] 
**connectivity** | [**ClusterConnectivity**](ClusterConnectivity.md) | Whether AstroPulse can currently reach and manage this cluster; omitted before its AstroPulse agent first connects and while the cluster does not exist. A registered cluster whose agent is reporting but cannot carry requests is Disconnected. | [optional] 
**connectivity_notice** | [**Notice**](Notice.md) | ConnectivityReason as a notice, with the one step that resolves it when there is one; absent when connectivityReason is empty. | [optional] 
**connectivity_reason** | **str** | Says why Connectivity is not Connected, such as an agent that cannot carry requests or a missing stored key, and what to do; empty otherwise. | [optional] 
**control_plane_node** | [**NodeGroup**](NodeGroup.md) | Represents the control plane node configuration (read-only in GET response). Includes the availability zones where the control plane is deployed. eks: auto-selected control plane AZs (first 3 sorted zones in region). gke: cluster-level zones from the regional cluster. aks: omitted because the control plane is fully managed by Azure and zones are not user-visible. selfHosted: zones match the control plane node group specification. | [optional] 
**created_timestamp** | **datetime** | The timestamp when the cluster was first created | [optional] 
**current_operation** | [**ClusterOperation**](ClusterOperation.md) | The operation running on the cluster now and the step it is on. Omitted when none runs. | [optional] 
**exists** | **bool** | Says whether the cluster is there to use: false while it is being created or registered, when a create stopped before the cluster existed or a registration failed, and once it is deleted or unregistered. | [optional] 
**exposure** | [**ClusterExposure**](ClusterExposure.md) | How this cluster exposes applications over TLS: the ClusterIssuer their certificates come from and whether the cluster&#39;s agent observed it Ready, who runs cert-manager and external-dns, and whether an exposed application takes the gateway path. Reported on a single-cluster read only. | [optional] 
**group** | [**ClusterGroup**](ClusterGroup.md) | The group of the fleet view the cluster belongs to, decided by its state; a fleet&#39;s counts are its clusters&#39; groups. | [optional] 
**kubeconfig_access** | [**KubeconfigAccess**](KubeconfigAccess.md) | Says how a kubeconfig generated for this cluster signs in and which lifetimes it can be generated with. | [optional] 
**kubernetes_version** | **str** | The version of Kubernetes running on the cluster | [optional] 
**labels** | **Dict[str, str]** | The key/value pairs attached to the cluster when it was registered. | [optional] 
**last_cancellation** | [**ClusterCancellation**](ClusterCancellation.md) | The last cancel of an operation on the cluster and what it removed. Omitted when none was cancelled since the last operation started. Present on a single-cluster read. | [optional] 
**last_seen** | **str** | The RFC 3339 timestamp when the AstroPulse agent on this cluster last reported in, empty if it never has. It can be recent while Connectivity is Disconnected (see ConnectivityReason). | [optional] 
**last_updated_timestamp** | **datetime** | The timestamp of the last update to the cluster | [optional] 
**latest_agent_version** | **str** | The latest available agent version from the container registry. Only populated for registered clusters. Compare with agentVersion to detect outdated agents. | [optional] 
**observed_nodes** | [**ClusterObservedNodes**](ClusterObservedNodes.md) | The cluster&#39;s nodes as its agent last reported them, grouped by pool, beside the node groups declared in workerNodes. Omitted when there is no report to show; observedNodesUnavailable says why. | [optional] 
**observed_nodes_unavailable** | [**ObservedNodesUnavailableReason**](ObservedNodesUnavailableReason.md) | Why observedNodes is omitted. Empty when observedNodes is present. | [optional] 
**observed_nodes_unavailable_message** | **str** | One sentence saying why observedNodes is omitted. Set whenever observedNodesUnavailable is. | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud the cluster runs in; absent for a cluster outside a cloud, or one whose cloud is not known. | [optional] 
**provisioner_type** | [**ProvisionerType**](ProvisionerType.md) | The provisioner and its configuration. | [optional] 
**region** | **str** | The geographical region where the cluster is deployed | [optional] 
**registry_access** | **List[str]** | Says which private images the cluster&#39;s nodes pull with no secret, and what to grant for others. | [optional] 
**release_channel** | [**GKEReleaseChannel**](GKEReleaseChannel.md) | The GKE release channel the cluster is enrolled in. Empty for non-GKE clusters. | [optional] 
**resource_group** | **str** | The Azure resource group for AKS clusters. Used to generate cleanup commands after cluster deletion. | [optional] 
**rollback_status** | [**AttemptStatusInfo**](AttemptStatusInfo.md) | The status of the last/current rollback attempt. | [optional] 
**state** | [**ClusterStatus**](ClusterStatus.md) | Represents the current state of the cluster. | [optional] 
**state_tone** | [**StateTone**](StateTone.md) | How state reads at a glance. | [optional] 
**status_notice** | [**Notice**](Notice.md) | Says what a failed state means and the one step that resolves it; absent when the state is not a failure. | [optional] 
**status_reason** | **str** | Explains the cluster&#39;s current state when an operation failed: what failed and how to fix it. Empty when the state needs no reason. | [optional] 
**total_monthly_cost** | **str** | Represents the estimated monthly cost of the cluster | [optional] 
**update_available** | **bool** | Indicates that a newer agent version is available and the cluster should be re-registered to update it (astroctl infra k8s register --cluster-name &lt;name&gt;). | [optional] 
**upgrade** | [**ClusterUpgradeOffer**](ClusterUpgradeOffer.md) | The Kubernetes upgrade AstroPulse offers this cluster. Omitted while an operation runs or when it cannot be determined right now. | [optional] 
**upgrade_status** | [**AttemptStatusInfo**](AttemptStatusInfo.md) | The status of the last/current upgrade attempt. | [optional] 
**version_support** | [**ClusterVersionSupport**](ClusterVersionSupport.md) | Reports whether AstroPulse can still manage this cluster at its current Kubernetes version. Present on a single-cluster read. | [optional] 
**worker_nodes** | [**List[NodeGroup]**](NodeGroup.md) | Represents the worker node configurations. Each node group includes the availability zones where it is deployed. | [optional] 
**workload_identity** | [**WorkloadIdentityStatus**](WorkloadIdentityStatus.md) | Whether workloads on this cluster can sign in to its cloud as an identity of their own. Omitted for registered clusters and other cases where it isn&#39;t known. | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster import K8sCluster

# TODO update the JSON string below
json = "{}"
# create an instance of K8sCluster from a JSON string
k8s_cluster_instance = K8sCluster.from_json(json)
# print the JSON string representation of the object
print(K8sCluster.to_json())

# convert the object into a dict
k8s_cluster_dict = k8s_cluster_instance.to_dict()
# create an instance of K8sCluster from a dict
k8s_cluster_from_dict = K8sCluster.from_dict(k8s_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


