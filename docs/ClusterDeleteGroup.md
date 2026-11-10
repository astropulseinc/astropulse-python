# ClusterDeleteGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **bool** | True when the group has items kept or needing your action. | [optional] 
**confirmed** | **bool** | True when the items are what the delete did, false when they are what it would do. | [optional] 
**items** | [**List[ClusterDeleteItem]**](ClusterDeleteItem.md) | The group&#39;s items, those kept or needing action first; it may be capped, with the rest named by moreSummary. | [optional] 
**kind** | [**ClusterDeleteGroupKind**](ClusterDeleteGroupKind.md) | The group&#39;s kind. | [optional] 
**listed** | **bool** | False when the group&#39;s items could not be listed; it never means there are none. | [optional] 
**listed_at** | **datetime** | When the group&#39;s items were listed. | [optional] 
**more_summary** | **str** | Names the items past the cap, such as \&quot;and 450 more\&quot;, when the list is capped. | [optional] 
**stale** | **bool** | True when that list is older than it should be, so an item may have changed since. | [optional] 
**summary** | **str** | One line for the group, such as \&quot;34 removed, 3 kept\&quot;. | [optional] 
**title** | **str** | Names the group, such as \&quot;Volumes\&quot;. | [optional] 
**total** | **int** | How many items the group has, including any not in items. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_delete_group import ClusterDeleteGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDeleteGroup from a JSON string
cluster_delete_group_instance = ClusterDeleteGroup.from_json(json)
# print the JSON string representation of the object
print(ClusterDeleteGroup.to_json())

# convert the object into a dict
cluster_delete_group_dict = cluster_delete_group_instance.to_dict()
# create an instance of ClusterDeleteGroup from a dict
cluster_delete_group_from_dict = ClusterDeleteGroup.from_dict(cluster_delete_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


