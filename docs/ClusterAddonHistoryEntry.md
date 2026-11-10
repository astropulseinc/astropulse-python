# ClusterAddonHistoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | When this version was applied, RFC 3339. | [optional] 
**created_by_display** | **str** | Names whoever applied it. | [optional] 
**current** | **bool** | Marks the version installed right now. | [optional] 
**rollback_eligible** | **bool** | Marks a version this add-on can be rolled back to. | [optional] 
**state** | [**ApplicationVersionState**](ApplicationVersionState.md) | How this version ended: whether it converged, failed, or is still settling. | [optional] 
**unavailable_reason** | **str** | Says why this version cannot be rolled back to; set whenever rollbackEligible is false. | [optional] 
**version** | **str** | This entry&#39;s version as vN; a rollback to it takes N as its target version. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_history_entry import ClusterAddonHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonHistoryEntry from a JSON string
cluster_addon_history_entry_instance = ClusterAddonHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonHistoryEntry.to_json())

# convert the object into a dict
cluster_addon_history_entry_dict = cluster_addon_history_entry_instance.to_dict()
# create an instance of ClusterAddonHistoryEntry from a dict
cluster_addon_history_entry_from_dict = ClusterAddonHistoryEntry.from_dict(cluster_addon_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


