# ObservedNodePool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change** | [**ObservedNodePoolChange**](ObservedNodePoolChange.md) | Says what is happening to the pool&#39;s nodes right now, from what the cluster reports: nodes being reclaimed, removed or replaced, cordoned nodes, or more nodes than the group&#39;s maximum. Absent when nothing is. | [optional] 
**kind** | [**ObservedNodePoolKind**](ObservedNodePoolKind.md) | Why the pool&#39;s nodes exist. | [optional] 
**label** | **str** | Names the pool for a person: what its nodes are for and how they come and go, for example \&quot;GPU pool (autoscaled)\&quot; or \&quot;Node group platform\&quot;. | [optional] 
**name** | **str** | The pool&#39;s name on the cluster: the node group&#39;s, or the autoscaling node pool&#39;s. | [optional] 
**node_group** | **str** | The name of the node group in workerNodes this pool is, when it is one of them. | [optional] 
**sets** | [**List[ObservedNodeSet]**](ObservedNodeSet.md) | Group the pool&#39;s nodes by machine type, capacity type and zone. | [optional] 
**truncated** | **bool** | True when the pool has more sets than are listed. | [optional] 

## Example

```python
from astropulse._generated.models.observed_node_pool import ObservedNodePool

# TODO update the JSON string below
json = "{}"
# create an instance of ObservedNodePool from a JSON string
observed_node_pool_instance = ObservedNodePool.from_json(json)
# print the JSON string representation of the object
print(ObservedNodePool.to_json())

# convert the object into a dict
observed_node_pool_dict = observed_node_pool_instance.to_dict()
# create an instance of ObservedNodePool from a dict
observed_node_pool_from_dict = ObservedNodePool.from_dict(observed_node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


