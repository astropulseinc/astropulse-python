# ClusterDeleteItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | A short description of the item, such as \&quot;20Gi, gp3\&quot;. | [optional] 
**id** | **str** | Your cloud provider&#39;s id for the item, shown when you ask for more detail. | [optional] 
**name** | **str** | The item&#39;s name. | [optional] 
**namespace** | **str** | The item&#39;s namespace, when it has one. | [optional] 
**outcome** | [**ClusterDeleteOutcome**](ClusterDeleteOutcome.md) | What the delete does with the item. | [optional] 
**reason** | **str** | Says why the item is kept or what to do about it. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_delete_item import ClusterDeleteItem

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDeleteItem from a JSON string
cluster_delete_item_instance = ClusterDeleteItem.from_json(json)
# print the JSON string representation of the object
print(ClusterDeleteItem.to_json())

# convert the object into a dict
cluster_delete_item_dict = cluster_delete_item_instance.to_dict()
# create an instance of ClusterDeleteItem from a dict
cluster_delete_item_from_dict = ClusterDeleteItem.from_dict(cluster_delete_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


