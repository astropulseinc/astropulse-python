# ObservedNodePoolChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Says it in one sentence, for example \&quot;Replacing a Spot node the cloud is reclaiming.\&quot; | [optional] 
**reason** | [**ObservedNodePoolChangeReason**](ObservedNodePoolChangeReason.md) | What the cluster reports is happening to the pool&#39;s nodes. | [optional] 

## Example

```python
from astropulse._generated.models.observed_node_pool_change import ObservedNodePoolChange

# TODO update the JSON string below
json = "{}"
# create an instance of ObservedNodePoolChange from a JSON string
observed_node_pool_change_instance = ObservedNodePoolChange.from_json(json)
# print the JSON string representation of the object
print(ObservedNodePoolChange.to_json())

# convert the object into a dict
observed_node_pool_change_dict = observed_node_pool_change_instance.to_dict()
# create an instance of ObservedNodePoolChange from a dict
observed_node_pool_change_from_dict = ObservedNodePoolChange.from_dict(observed_node_pool_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


