# ClusterAddonMetricsSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | The Application serving the add-on. | [optional] 
**cluster_name** | **str** | The cluster the add-on runs on. | [optional] 
**points** | [**List[MetricsSeriesPoint]**](MetricsSeriesPoint.md) | The samples in the window, oldest first. | [optional] 
**window** | [**CostWindow**](CostWindow.md) | The time range these points cover. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_metrics_series import ClusterAddonMetricsSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonMetricsSeries from a JSON string
cluster_addon_metrics_series_instance = ClusterAddonMetricsSeries.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonMetricsSeries.to_json())

# convert the object into a dict
cluster_addon_metrics_series_dict = cluster_addon_metrics_series_instance.to_dict()
# create an instance of ClusterAddonMetricsSeries from a dict
cluster_addon_metrics_series_from_dict = ClusterAddonMetricsSeries.from_dict(cluster_addon_metrics_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


