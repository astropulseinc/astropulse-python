# ClusterStorageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterStorage**](ClusterStorage.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_storage_response import ClusterStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStorageResponse from a JSON string
cluster_storage_response_instance = ClusterStorageResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterStorageResponse.to_json())

# convert the object into a dict
cluster_storage_response_dict = cluster_storage_response_instance.to_dict()
# create an instance of ClusterStorageResponse from a dict
cluster_storage_response_from_dict = ClusterStorageResponse.from_dict(cluster_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


