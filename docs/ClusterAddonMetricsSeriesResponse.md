# ClusterAddonMetricsSeriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAddonMetricsSeries**](ClusterAddonMetricsSeries.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_metrics_series_response import ClusterAddonMetricsSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonMetricsSeriesResponse from a JSON string
cluster_addon_metrics_series_response_instance = ClusterAddonMetricsSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonMetricsSeriesResponse.to_json())

# convert the object into a dict
cluster_addon_metrics_series_response_dict = cluster_addon_metrics_series_response_instance.to_dict()
# create an instance of ClusterAddonMetricsSeriesResponse from a dict
cluster_addon_metrics_series_response_from_dict = ClusterAddonMetricsSeriesResponse.from_dict(cluster_addon_metrics_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


