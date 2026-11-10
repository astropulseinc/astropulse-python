# ClusterProgressPageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterProgressPage**](ClusterProgressPage.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_progress_page_response import ClusterProgressPageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProgressPageResponse from a JSON string
cluster_progress_page_response_instance = ClusterProgressPageResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterProgressPageResponse.to_json())

# convert the object into a dict
cluster_progress_page_response_dict = cluster_progress_page_response_instance.to_dict()
# create an instance of ClusterProgressPageResponse from a dict
cluster_progress_page_response_from_dict = ClusterProgressPageResponse.from_dict(cluster_progress_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


