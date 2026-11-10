# ClusterAddonResyncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Reports whether the resync was forced past an in-flight operation. | [optional] 
**message** | **str** | Says what happened, in words to show a person. | [optional] 
**status** | [**ApplicationResyncStatus**](ApplicationResyncStatus.md) | What the request did; absent when it could not be told. | [optional] 
**type** | [**ClusterAddonType**](ClusterAddonType.md) | The add-on&#39;s public name. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_resync_response import ClusterAddonResyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonResyncResponse from a JSON string
cluster_addon_resync_response_instance = ClusterAddonResyncResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonResyncResponse.to_json())

# convert the object into a dict
cluster_addon_resync_response_dict = cluster_addon_resync_response_instance.to_dict()
# create an instance of ClusterAddonResyncResponse from a dict
cluster_addon_resync_response_from_dict = ClusterAddonResyncResponse.from_dict(cluster_addon_resync_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


