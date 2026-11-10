# NodeGroupRemoval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** | True when an update can remove the node group. | [optional] 
**notice** | [**Notice**](Notice.md) | Says why the node group can&#39;t be removed and the next step, when there is one; absent when it can be removed. | [optional] 

## Example

```python
from astropulse._generated.models.node_group_removal import NodeGroupRemoval

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupRemoval from a JSON string
node_group_removal_instance = NodeGroupRemoval.from_json(json)
# print the JSON string representation of the object
print(NodeGroupRemoval.to_json())

# convert the object into a dict
node_group_removal_dict = node_group_removal_instance.to_dict()
# create an instance of NodeGroupRemoval from a dict
node_group_removal_from_dict = NodeGroupRemoval.from_dict(node_group_removal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


