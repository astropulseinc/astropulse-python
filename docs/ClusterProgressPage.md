# ClusterProgressPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Continues the listing when passed back as pageToken; empty on the last page. | [optional] 
**operations** | [**List[ClusterProgress]**](ClusterProgress.md) | This page, newest first. | [optional] 
**total_count** | **int** | How many operations match in total. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_progress_page import ClusterProgressPage

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProgressPage from a JSON string
cluster_progress_page_instance = ClusterProgressPage.from_json(json)
# print the JSON string representation of the object
print(ClusterProgressPage.to_json())

# convert the object into a dict
cluster_progress_page_dict = cluster_progress_page_instance.to_dict()
# create an instance of ClusterProgressPage from a dict
cluster_progress_page_from_dict = ClusterProgressPage.from_dict(cluster_progress_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


