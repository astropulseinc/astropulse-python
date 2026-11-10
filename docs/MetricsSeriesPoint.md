# MetricsSeriesPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | [**AcceleratorMetrics**](AcceleratorMetrics.md) | What the accelerators the application&#39;s pods hold did over the window, present only for an application actually holding a device while the accelerator-metrics add-on is installed. | [optional] 
**average_cpu_cores_used** | **float** | The CPU the application used across the window. | [optional] 
**complete** | **bool** | False when the collector could not obtain a measurement for every workload instance it expected this window. Render as partial, never averaged in as if whole. | [optional] 
**inference** | [**InferenceMetrics**](InferenceMetrics.md) | What the serving runtime measured, present only for an application that serves a model. | [optional] 
**memory_working_set_bytes** | **float** | The memory it held. | [optional] 
**network_receive_bytes_per_second** | **float** | The network receive and transmit rates are absent (not zero) whenever the active source cannot observe network — never present when Source is \&quot;metrics-api\&quot;. A zero here would render as \&quot;this application sent no traffic,\&quot; which looks exactly like an outage on a usage graph. | [optional] 
**network_transmit_bytes_per_second** | **float** |  | [optional] 
**queue** | [**QueueMetrics**](QueueMetrics.md) | What the cluster&#39;s workload queue did with the application&#39;s replicas, present only for an application whose pods name a queue while the workload-queueing add-on is installed. | [optional] 
**source** | **str** | Names which Kubernetes-native tier produced this point: kubelet-summary, metrics-api, or prometheus. Only kubelet-summary ever carries network. | [optional] 
**window_end** | **str** | When it closed. | [optional] 
**window_start** | **str** | When this sample&#39;s window opened. | [optional] 

## Example

```python
from astropulse._generated.models.metrics_series_point import MetricsSeriesPoint

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsSeriesPoint from a JSON string
metrics_series_point_instance = MetricsSeriesPoint.from_json(json)
# print the JSON string representation of the object
print(MetricsSeriesPoint.to_json())

# convert the object into a dict
metrics_series_point_dict = metrics_series_point_instance.to_dict()
# create an instance of MetricsSeriesPoint from a dict
metrics_series_point_from_dict = MetricsSeriesPoint.from_dict(metrics_series_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


