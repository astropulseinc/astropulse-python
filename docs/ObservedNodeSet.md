# ObservedNodeSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_type** | [**InstanceType**](InstanceType.md) | How the nodes are bought. Omitted when the provider does not state it. | [optional] 
**cordoned** | **int** | How many of them take no new workloads while nothing says they are being removed. Omitted when none. | [optional] 
**count** | **int** | How many nodes are in the set. | [optional] 
**draining** | **int** | How many of them are being drained to leave the cluster: the cloud is reclaiming or stopping them, an autoscaler is removing them, or they are being deleted. Omitted when none. | [optional] 
**gpus** | [**List[ObservedNodeGPU]**](ObservedNodeGPU.md) | The accelerators on each node of the set. | [optional] 
**machine_type** | **str** | The nodes&#39; machine type, for example g6.xlarge. Omitted when the nodes do not say. | [optional] 
**ready** | **int** | How many of them are ready. Omitted when not reported. | [optional] 
**zone** | **str** | The nodes&#39; availability zone. Omitted when the nodes do not say. | [optional] 

## Example

```python
from astropulse._generated.models.observed_node_set import ObservedNodeSet

# TODO update the JSON string below
json = "{}"
# create an instance of ObservedNodeSet from a JSON string
observed_node_set_instance = ObservedNodeSet.from_json(json)
# print the JSON string representation of the object
print(ObservedNodeSet.to_json())

# convert the object into a dict
observed_node_set_dict = observed_node_set_instance.to_dict()
# create an instance of ObservedNodeSet from a dict
observed_node_set_from_dict = ObservedNodeSet.from_dict(observed_node_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


