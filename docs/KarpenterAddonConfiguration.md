# KarpenterAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_accelerators** | **List[str]** | The GPU models GPU nodes may have, as the machine catalog names them, such as l4 or a10g. Left out, every model is allowed. | [optional] 
**ami_alias** | **str** | The machine image new nodes start from, as family@version such as al2023@v20260818; changing it replaces existing nodes. Left out, AstroPulse&#39;s default applies; with the GPU node pool on, pin a version rather than @latest. | [optional] 
**aws** | [**AWSAddonConfig**](AWSAddonConfig.md) | Node Autoscaling&#39;s AWS settings, on EKS only. | [optional] 
**cpu_capacity_types** | [**List[InstanceType]**](InstanceType.md) | How the default pool&#39;s nodes may be bought; Spot costs less but needs the interruption queue. Left out, it keeps the last value set, or buys both, Spot first, where the cluster has the queue and &#x60;OnDemand&#x60; elsewhere. | [optional] 
**cpu_limit** | **int** | The most CPU cores the default node pool may run in total, from 1 to 100000; pods wait once it is reached. | [optional] [default to 100]
**disruption** | [**KarpenterDisruption**](KarpenterDisruption.md) | When nodes in the default pool are removed or replaced to save cost. | [optional] 
**enable_gpu_node_pool** | **bool** | Lets Node Autoscaling start GPU nodes. They take only pods that tolerate nvidia.com/gpu:NoSchedule, and AstroPulse runs the NVIDIA device plugin on them, so remove any you installed yourself. | [optional] 
**gpu_capacity_reservations** | [**KarpenterCapacityReservations**](KarpenterCapacityReservations.md) | EC2 capacity reservations, Capacity Blocks included, that GPU nodes use before Spot or On-Demand. On a cluster AstroPulse created, each is checked before install to exist, be active, be a g or p instance type of generation 4 or later, and be in one of the cluster&#39;s zones. | [optional] 
**gpu_capacity_types** | [**List[InstanceType]**](InstanceType.md) | How GPU nodes may be bought; Spot costs less, but a node can be reclaimed at short notice and needs &#x60;interruptionQueue&#x60; on a registered cluster. Left out, a new pool buys &#x60;OnDemand&#x60; and an existing one keeps its current value. | [optional] 
**gpu_disruption** | [**KarpenterDisruption**](KarpenterDisruption.md) | When GPU nodes are removed or replaced to save cost; &#x60;gpuLimit&#x60; still caps GPU spend. | [optional] 
**gpu_instance_families** | **List[str]** | The instance families GPU nodes may use, such as g6 or g5, at most 32. | [optional] 
**gpu_instance_sizes** | **List[str]** | The instance sizes GPU nodes may use, such as xlarge or 2xlarge, at most 32. | [optional] 
**gpu_limit** | **int** | The most GPUs the GPU node pool may run in total, from 1 to 1000. | [optional] [default to 10]
**gpu_max_memory_gi_b_per_node** | **int** | The most memory one GPU node may have, in GiB, from 1 to 32768. | [optional] 
**gpu_max_vcpu_per_node** | **int** | The most CPU cores one GPU node may have, from 1 to 1024. Left out, the smallest size that fits each workload and your quota is chosen. | [optional] 
**gpu_node_drain_timeout** | **str** | How long a GPU node being removed waits for its pods to finish, up to 24h, or &#x60;None&#x60; for no limit. Left out, a new pool uses 1h and an existing one keeps its current value. | [optional] 
**gpu_node_expiry** | **str** | How long a GPU node runs before it is replaced, even while busy: &#x60;Never&#x60;, or days or hours such as 30d or 12h. Left out, a new pool uses &#x60;Never&#x60; and an existing one keeps its current value. | [optional] 
**interruption_queue** | **bool** | Turn on when your registered cluster has Node Autoscaling&#39;s interruption queue, from the prerequisites stack AstroPulse generates: Spot nodes are then drained before they are reclaimed, and Spot may be bought. Clusters AstroPulse created always have it. | [optional] 
**memory_limit** | **str** | The most memory the default node pool may run in total, such as 400Gi; the pool stops adding nodes at this or &#x60;cpuLimit&#x60;, whichever comes first. | [optional] [default to '400Gi']
**service_account_name** | **str** | The Kubernetes service account Node Autoscaling runs as. Left out, AstroPulse&#39;s default applies. | [optional] 

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


