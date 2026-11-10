# NodeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | [**AcceleratorAttachment**](AcceleratorAttachment.md) | Requests accelerator hardware for this node group (optional). Exactly one member of the union must be set; gpu is the supported member. Not available on selfHosted clusters. | [optional] 
**availability_zones** | **List[str]** | The list of availability zones for this node group (optional). Default behavior: if omitted, the server auto-selects the first 3 sorted zones in the region (or fewer if the region has &lt; 3 zones). For aks, Azure manages zone placement automatically. Constraints:   - Maximum 3 zones per node group.   - Zones must be valid for the cluster&#39;s region (validated server-side).   - Zones must be a subset of the cluster/control plane zones (eks, gke).   - Zones are immutable after creation — changing zones requires deleting and recreating the node group. Example for eks: [\&quot;us-west-2a\&quot;, \&quot;us-west-2b\&quot;] Example for gke: [\&quot;us-central1-a\&quot;, \&quot;us-central1-b\&quot;, \&quot;us-central1-c\&quot;] | [optional] 
**capacity_block** | [**CapacityBlockStatus**](CapacityBlockStatus.md) | The Capacity Block a CapacityBlock node group runs on (read-only; ignored on input). | [optional] 
**disk_size_gb** | **int** | The root disk of every node in this group, in whole gigabytes (optional). It holds the operating system, the images the node pulls and anything written to the node&#39;s local disk, including the model weight cache. Accepted range: 20 to 16384 on eks and selfHosted, 20 to 65536 on gke, 30 to 2048 on aks; omitted, the provider&#39;s default applies (100 on eks and gke, 20 on selfHosted, the machine type&#39;s own size on aks). Changing it replaces the group&#39;s nodes, and is refused on gke. | [optional] 
**instance_type** | [**InstanceType**](InstanceType.md) | How the node group&#39;s nodes are bought; OnDemand when omitted. It cannot change on an existing node group. | 
**labels** | **Dict[str, str]** | Kubernetes labels applied to nodes in this group (optional), such as {\&quot;tier\&quot;: \&quot;frontend\&quot;, \&quot;team.example.com/owner\&quot;: \&quot;ml\&quot;}. Keys are Kubernetes label keys, not under kubernetes.io or k8s.io (at most 63 characters in all on eks); values are 1-63 letters, digits, &#39;-&#39;, &#39;_&#39; and &#39;.&#39;, starting and ending with a letter or digit. | [optional] 
**machine_types** | **List[str]** | The list of machine types for nodes. Provider-specific formats: eks (e.g. \&quot;t3.medium\&quot;), gke (e.g. \&quot;n1-standard-1\&quot;), aks (e.g. \&quot;Standard_D2s_v3\&quot;). Required unless Accelerator is set. Supplying only machineTypes keeps explicit machine selection; supplying only accelerator lets AstroPulse resolve compatible machine types; supplying both requires every listed machine to satisfy the accelerator; supplying neither is invalid. Multiple entries are honoured on eks, where the node group may draw from every listed type. gke, aks and selfHosted node groups run a single machine type — supply exactly one there; a longer list is rejected. | [optional] 
**max_node** | **int** | The maximum number of nodes in the group (required, minimum: 1). Must be &gt;&#x3D; MinNode. For control plane node groups, must be an odd number.  On gke, aks and selfHosted the provider&#39;s autoscaler scales the group between minNode and maxNode. On eks maxNode has no effect: the group runs at minNode, and elastic capacity, GPUs included, comes from the karpenter add-on. | 
**min_node** | **int** | The minimum number of nodes in the group. Must be &lt;&#x3D; MaxNode.  Zero means the group holds no nodes while idle and is scaled up when a pod needs one, which is only honoured where an autoscaler watches the group: gke, aks (except its first node group, which becomes the system pool), and selfHosted. It is rejected on eks, where managed node groups are fixed capacity and Karpenter provides elastic capacity instead.  To undo it, set minNode back to 1 or more and apply again — the same update path, no separate operation. | [optional] 
**name** | **str** | The node group name (required, 1-50 characters, valid DNS name). Format: lowercase alphanumeric and hyphens, must start with a letter. Example: \&quot;ng-workers-1\&quot; | 
**removal** | [**NodeGroupRemoval**](NodeGroupRemoval.md) | Says whether an update can remove this node group now (read-only; ignored on input). Present on worker node groups. | [optional] 
**state** | [**NodeGroupState**](NodeGroupState.md) | Adding while a running update creates the node group, and absent otherwise (read-only; ignored on input). | [optional] 
**taints** | [**List[Tainted]**](Tainted.md) | Kubernetes taints applied to nodes in this group (optional) | [optional] 

## Example

```python
from astropulse._generated.models.node_group import NodeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroup from a JSON string
node_group_instance = NodeGroup.from_json(json)
# print the JSON string representation of the object
print(NodeGroup.to_json())

# convert the object into a dict
node_group_dict = node_group_instance.to_dict()
# create an instance of NodeGroup from a dict
node_group_from_dict = NodeGroup.from_dict(node_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


