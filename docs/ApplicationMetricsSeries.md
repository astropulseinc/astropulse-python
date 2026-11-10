# ApplicationMetricsSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator_summary** | [**AcceleratorMetricsSummary**](AcceleratorMetricsSummary.md) | What the application&#39;s accelerators did across the whole window, present only for an application holding a device. Use it for the range&#39;s figures: a point describes its own window. | [optional] 
**application_name** | **str** | The application&#39;s own name. | [optional] 
**cluster_id** | **str** | Identifies that cluster. | [optional] 
**cluster_name** | **str** | The cluster the application runs on. | [optional] 
**generated_app_name** | **str** | The name AstroPulse gave the workload in-cluster. | [optional] 
**inference_summary** | [**InferenceMetricsSummary**](InferenceMetricsSummary.md) | The model&#39;s behaviour across the whole window, present only for an application that serves one. Use it for \&quot;the p99 over this range\&quot;: the per-point percentiles describe their own windows and must never be averaged together. | [optional] 
**points** | [**List[MetricsSeriesPoint]**](MetricsSeriesPoint.md) | The samples in the window, oldest first. A window with no stored sample is absent rather than reported as zero. | [optional] 
**queue_summary** | [**QueueMetricsSummary**](QueueMetricsSummary.md) | The application&#39;s life in its workload queue across the whole window, present only for an application whose pods name a queue. | [optional] 
**window** | [**CostWindow**](CostWindow.md) | The time range these points cover. | [optional] 

## Example

```python
from astropulse._generated.models.application_metrics_series import ApplicationMetricsSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetricsSeries from a JSON string
application_metrics_series_instance = ApplicationMetricsSeries.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetricsSeries.to_json())

# convert the object into a dict
application_metrics_series_dict = application_metrics_series_instance.to_dict()
# create an instance of ApplicationMetricsSeries from a dict
application_metrics_series_from_dict = ApplicationMetricsSeries.from_dict(application_metrics_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


