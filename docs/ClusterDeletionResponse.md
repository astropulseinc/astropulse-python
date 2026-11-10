# ClusterDeletionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterDeletion**](ClusterDeletion.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_deletion_response import ClusterDeletionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDeletionResponse from a JSON string
cluster_deletion_response_instance = ClusterDeletionResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterDeletionResponse.to_json())

# convert the object into a dict
cluster_deletion_response_dict = cluster_deletion_response_instance.to_dict()
# create an instance of ClusterDeletionResponse from a dict
cluster_deletion_response_from_dict = ClusterDeletionResponse.from_dict(cluster_deletion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


