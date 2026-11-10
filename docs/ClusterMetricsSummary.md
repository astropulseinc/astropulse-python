# ClusterMetricsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_count** | **int** | Every platform-managed application deployed to the cluster, regardless of whether it reported in this window. | [optional] 
**cluster_id** | **str** | Identifies the cluster. | [optional] 
**cluster_name** | **str** | Its name. | [optional] 
**complete** | **bool** | False if any one reporting application had a sample with partial coverage — the collector could not reach every workload instance it expected. True when there were zero incomplete samples, including when there were zero samples at all. | [optional] 
**empty_message** | **str** | Says why no application reported usage in the window and what to do next. Set only when none did. | [optional] 
**last_received_at** | **str** | The most recent sample window-end across every reporting application, absent when nothing reported. | [optional] 
**reporting_application_count** | **int** | The subset of ApplicationCount that had at least one stored sample in the window. The gap between the two counts is exactly how many applications reported nothing — never inferred from a zero reading. | [optional] 
**sample_count** | **int** | The total stored samples every reporting application contributed in the window. | [optional] 
**totals** | [**MetricsDimensions**](MetricsDimensions.md) | What every reporting application added up to. | [optional] 
**window** | [**CostWindow**](CostWindow.md) | The time range this summary covers. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_metrics_summary import ClusterMetricsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetricsSummary from a JSON string
cluster_metrics_summary_instance = ClusterMetricsSummary.from_json(json)
# print the JSON string representation of the object
print(ClusterMetricsSummary.to_json())

# convert the object into a dict
cluster_metrics_summary_dict = cluster_metrics_summary_instance.to_dict()
# create an instance of ClusterMetricsSummary from a dict
cluster_metrics_summary_from_dict = ClusterMetricsSummary.from_dict(cluster_metrics_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


