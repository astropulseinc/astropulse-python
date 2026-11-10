# ClusterAddonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAddon**](ClusterAddon.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_response import ClusterAddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonResponse from a JSON string
cluster_addon_response_instance = ClusterAddonResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonResponse.to_json())

# convert the object into a dict
cluster_addon_response_dict = cluster_addon_response_instance.to_dict()
# create an instance of ClusterAddonResponse from a dict
cluster_addon_response_from_dict = ClusterAddonResponse.from_dict(cluster_addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


