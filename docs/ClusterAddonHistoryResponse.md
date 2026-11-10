# ClusterAddonHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | The Application serving this add-on on the cluster. | [optional] 
**current_version** | **str** | The version installed right now, as vN. | [optional] 
**entries** | [**List[ClusterAddonHistoryEntry]**](ClusterAddonHistoryEntry.md) | The versions this add-on has run, newest first. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Say what this history could not confirm, such as which versions can still be rolled back to; absent when there is nothing to say. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_history_response import ClusterAddonHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonHistoryResponse from a JSON string
cluster_addon_history_response_instance = ClusterAddonHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonHistoryResponse.to_json())

# convert the object into a dict
cluster_addon_history_response_dict = cluster_addon_history_response_instance.to_dict()
# create an instance of ClusterAddonHistoryResponse from a dict
cluster_addon_history_response_from_dict = ClusterAddonHistoryResponse.from_dict(cluster_addon_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


