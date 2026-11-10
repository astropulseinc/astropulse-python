# ClusterAddonAcceleratorReadiness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**declared_accelerators** | **int** | How many NVIDIA devices the cluster&#39;s node groups can ever run. Zero on a cluster with no accelerator node group. | [optional] 
**gpu_nodes** | **str** | Says how many NVIDIA GPU nodes the cluster runs now and in which pools, or \&quot;Nothing to check yet: no GPU nodes\&quot;. Empty when the cluster has not reported its nodes. | [optional] 
**karpenter_gpu_pool** | **bool** | Reports a configured GPU node pool (the Karpenter add-on&#39;s or EKS Auto Mode&#39;s), which provisions accelerator nodes on demand: zero declared accelerators with this set is still a cluster that will produce measurements, once a GPU node exists. | [optional] 
**measurable** | **bool** | Whether anything on this cluster will report: an NVIDIA node group, or a GPU node pool. | [optional] 
**vendors** | **List[str]** | The accelerator vendors the cluster&#39;s node groups declare (nvidia, amd, google, xilinx), sorted. A vendor here that is not nvidia is why Warning is present. | [optional] 
**warning** | **str** | The one sentence to show when the install will work but measure nothing, or less than the cluster&#39;s accelerators suggest. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_accelerator_readiness import ClusterAddonAcceleratorReadiness

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonAcceleratorReadiness from a JSON string
cluster_addon_accelerator_readiness_instance = ClusterAddonAcceleratorReadiness.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonAcceleratorReadiness.to_json())

# convert the object into a dict
cluster_addon_accelerator_readiness_dict = cluster_addon_accelerator_readiness_instance.to_dict()
# create an instance of ClusterAddonAcceleratorReadiness from a dict
cluster_addon_accelerator_readiness_from_dict = ClusterAddonAcceleratorReadiness.from_dict(cluster_addon_accelerator_readiness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


