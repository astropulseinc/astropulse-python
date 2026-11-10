# ClusterMetricsSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterMetricsSummary**](ClusterMetricsSummary.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_metrics_summary_response import ClusterMetricsSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetricsSummaryResponse from a JSON string
cluster_metrics_summary_response_instance = ClusterMetricsSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterMetricsSummaryResponse.to_json())

# convert the object into a dict
cluster_metrics_summary_response_dict = cluster_metrics_summary_response_instance.to_dict()
# create an instance of ClusterMetricsSummaryResponse from a dict
cluster_metrics_summary_response_from_dict = ClusterMetricsSummaryResponse.from_dict(cluster_metrics_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


