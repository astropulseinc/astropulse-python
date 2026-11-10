# KarpenterAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_accelerators** | **List[str]** | Limits the GPU node pool to these GPU models, as the machine catalog names them (l4, a10g); omit it to allow every model. Leaving out the largest GPUs keeps the most expensive instances out of reach. | [optional] 
**ami_alias** | **str** | The machine image Node Autoscaling launches nodes from, as family@version (for example al2023@v20260818); omit it to take the AstroPulse default. Changing it replaces existing nodes, and with the GPU node pool enabled it must be pinned rather than a floating @latest, so GPU driver updates happen when you choose. | [optional] 
**aws** | [**AWSAddonConfig**](AWSAddonConfig.md) | The AWS-specific settings Node Autoscaling needs. EKS only. | [optional] 
**cpu_capacity_types** | [**List[InstanceType]**](InstanceType.md) | The purchase options the default node pool may buy: OnDemand, Spot or both; Spot needs the interruption queue (see interruptionQueue). Until it is set, the pool buys both, Spot first, where the cluster has the queue, and OnDemand elsewhere; an apply that leaves it out keeps the value it was last set to. | [optional] 
**cpu_limit** | **int** | The most vCPU the default node pool runs at once across its nodes (optional, 1-100000, default 100). It caps what the pool spends on CPU nodes; pods wait once it is reached. | [optional] [default to 100]
**disruption** | [**KarpenterDisruption**](KarpenterDisruption.md) | When nodes of the default pool are removed or replaced to save cost (optional; defaults: WhenEmptyOrUnderutilized, 5m, 10%). | [optional] 
**enable_gpu_node_pool** | **bool** | Lets Node Autoscaling provision GPU instances (optional, default false). GPU nodes are tainted nvidia.com/gpu:NoSchedule, so pods need a matching toleration; AstroPulse manages the NVIDIA device plugin on the pool&#39;s nodes, so remove or exclude any cluster-wide plugin you installed yourself. | [optional] 
**gpu_capacity_reservations** | [**KarpenterCapacityReservations**](KarpenterCapacityReservations.md) | The EC2 capacity reservations, Capacity Blocks included, that the GPU node pool fills before spot or on-demand (optional; requires enableGpuNodePool). Before installing, AstroPulse checks each exists in the cluster&#39;s account and region, is active, is a g or p instance type (generation 4 or later) and is in one of the cluster&#39;s zones. Registered clusters are not checked. | [optional] 
**gpu_capacity_types** | [**List[InstanceType]**](InstanceType.md) | The purchase options the GPU node pool may buy: OnDemand, Spot or both; a new pool buys OnDemand, and an existing one keeps what it buys unless this is set. Spot costs less, but a node can be reclaimed at short notice, restarting its pods, and needs interruptionQueue on a registered cluster. | [optional] 
**gpu_disruption** | [**KarpenterDisruption**](KarpenterDisruption.md) | When GPU nodes are removed or replaced to save cost (optional; defaults: WhenEmpty, 10m, 10%; requires enableGpuNodePool). gpuLimit stays the hard cap on GPU spend whatever these say. | [optional] 
**gpu_instance_families** | **List[str]** | Limits the GPU node pool to these instance families, such as g6 or g5 (optional, at most 32). | [optional] 
**gpu_instance_sizes** | **List[str]** | Limits the GPU node pool to these instance sizes, such as xlarge or 2xlarge (optional, at most 32). | [optional] 
**gpu_limit** | **int** | The maximum number of GPUs the GPU node pool may provision, counted across the pool (optional, 1-1000, default 10). Ignored unless the GPU node pool is enabled. | [optional] [default to 10]
**gpu_max_memory_gi_b_per_node** | **int** | The most memory one GPU node may have, in GiB (optional, 1-32768). | [optional] 
**gpu_max_vcpu_per_node** | **int** | The most vCPU one GPU node may have (optional, 1-1024); unset, the GPU pool picks the smallest sizes that fit each model and the account&#39;s quota. | [optional] 
**gpu_node_drain_timeout** | **str** | The most time a GPU node being removed waits for its pods before they are deleted: hours and minutes up to 24h, such as 1h, or None for no limit. A new pool uses 1h; an existing one keeps its own unless this is set. | [optional] 
**gpu_node_expiry** | **str** | How long a GPU node runs before it is replaced, even while busy: Never, or whole days or hours such as 30d or 12h. A new pool uses Never; an existing one keeps its own unless this is set. | [optional] 
**interruption_queue** | **bool** | Set to true when a registered cluster has Node Autoscaling&#39;s interruption queue, created by the Node Autoscaling prerequisites stack AstroPulse generates for your AWS account: nodes are drained before Spot reclaims them, the default pool may buy Spot, and gpuCapacityTypes may list spot. Clusters AstroPulse creates always have the queue. | [optional] 
**memory_limit** | **str** | The most memory the default node pool runs at once across its nodes, as a quantity such as 400Gi (optional, default 400Gi). The pool stops adding nodes at whichever of cpuLimit and memoryLimit it reaches first. | [optional] [default to '400Gi']
**service_account_name** | **str** | The Kubernetes service account Node Autoscaling runs as. Empty takes the AstroPulse default. | [optional] 

## Example

```python
from astropulse._generated.models.karpenter_addon_configuration import KarpenterAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of KarpenterAddonConfiguration from a JSON string
karpenter_addon_configuration_instance = KarpenterAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(KarpenterAddonConfiguration.to_json())

# convert the object into a dict
karpenter_addon_configuration_dict = karpenter_addon_configuration_instance.to_dict()
# create an instance of KarpenterAddonConfiguration from a dict
karpenter_addon_configuration_from_dict = KarpenterAddonConfiguration.from_dict(karpenter_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


