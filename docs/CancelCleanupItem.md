# CancelCleanupItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**CancelCleanupKind**](CancelCleanupKind.md) | The kind of resource. | [optional] 
**name** | **str** | The node group&#39;s name. | [optional] 
**notice** | [**Notice**](Notice.md) | Says what happened to the node group, why, and the one next step when it is still in the cluster. | [optional] 
**outcome** | [**CancelCleanupOutcome**](CancelCleanupOutcome.md) | Whether the node group was removed, never created, or is still in the cluster. | [optional] 

## Example

```python
from astropulse._generated.models.cancel_cleanup_item import CancelCleanupItem

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCleanupItem from a JSON string
cancel_cleanup_item_instance = CancelCleanupItem.from_json(json)
# print the JSON string representation of the object
print(CancelCleanupItem.to_json())

# convert the object into a dict
cancel_cleanup_item_dict = cancel_cleanup_item_instance.to_dict()
# create an instance of CancelCleanupItem from a dict
cancel_cleanup_item_from_dict = CancelCleanupItem.from_dict(cancel_cleanup_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


