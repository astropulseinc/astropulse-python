# SetClusterStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindings** | [**List[ClusterStorageBinding]**](ClusterStorageBinding.md) | The complete set of names for this cluster&#39;s storage. | 

## Example

```python
from astropulse._generated.models.set_cluster_storage_request import SetClusterStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetClusterStorageRequest from a JSON string
set_cluster_storage_request_instance = SetClusterStorageRequest.from_json(json)
# print the JSON string representation of the object
print(SetClusterStorageRequest.to_json())

# convert the object into a dict
set_cluster_storage_request_dict = set_cluster_storage_request_instance.to_dict()
# create an instance of SetClusterStorageRequest from a dict
set_cluster_storage_request_from_dict = SetClusterStorageRequest.from_dict(set_cluster_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


