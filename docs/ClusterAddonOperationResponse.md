# ClusterAddonOperationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAddonOperation**](ClusterAddonOperation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_operation_response import ClusterAddonOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonOperationResponse from a JSON string
cluster_addon_operation_response_instance = ClusterAddonOperationResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonOperationResponse.to_json())

# convert the object into a dict
cluster_addon_operation_response_dict = cluster_addon_operation_response_instance.to_dict()
# create an instance of ClusterAddonOperationResponse from a dict
cluster_addon_operation_response_from_dict = ClusterAddonOperationResponse.from_dict(cluster_addon_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


