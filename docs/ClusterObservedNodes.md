# ClusterObservedNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observed_at** | **datetime** | When the agent last reported, in RFC 3339. While the cluster is Disconnected it is the last report before that, and the pools may be out of date. | [optional] 
**pools** | [**List[ObservedNodePool]**](ObservedNodePool.md) | The cluster&#39;s node pools: its node groups and the pools an autoscaler launches nodes into. Empty when the agent reported no nodes. | [optional] 
**truncated** | **bool** | True when the cluster has more pools than are listed. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_observed_nodes import ClusterObservedNodes

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterObservedNodes from a JSON string
cluster_observed_nodes_instance = ClusterObservedNodes.from_json(json)
# print the JSON string representation of the object
print(ClusterObservedNodes.to_json())

# convert the object into a dict
cluster_observed_nodes_dict = cluster_observed_nodes_instance.to_dict()
# create an instance of ClusterObservedNodes from a dict
cluster_observed_nodes_from_dict = ClusterObservedNodes.from_dict(cluster_observed_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


