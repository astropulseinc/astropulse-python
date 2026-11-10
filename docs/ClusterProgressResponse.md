# ClusterProgressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterProgress**](ClusterProgress.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_progress_response import ClusterProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProgressResponse from a JSON string
cluster_progress_response_instance = ClusterProgressResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterProgressResponse.to_json())

# convert the object into a dict
cluster_progress_response_dict = cluster_progress_response_instance.to_dict()
# create an instance of ClusterProgressResponse from a dict
cluster_progress_response_from_dict = ClusterProgressResponse.from_dict(cluster_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


