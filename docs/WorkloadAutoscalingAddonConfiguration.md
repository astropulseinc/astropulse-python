# WorkloadAutoscalingAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics_source** | [**AutoscalingMetricsSource**](AutoscalingMetricsSource.md) | Where scaling reads a workload&#39;s own metrics, such as its request rate. Left out, a workload that would scale on such a metric scales on CPU instead. | [optional] 

## Example

```python
from astropulse._generated.models.workload_autoscaling_addon_configuration import WorkloadAutoscalingAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadAutoscalingAddonConfiguration from a JSON string
workload_autoscaling_addon_configuration_instance = WorkloadAutoscalingAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(WorkloadAutoscalingAddonConfiguration.to_json())

# convert the object into a dict
workload_autoscaling_addon_configuration_dict = workload_autoscaling_addon_configuration_instance.to_dict()
# create an instance of WorkloadAutoscalingAddonConfiguration from a dict
workload_autoscaling_addon_configuration_from_dict = WorkloadAutoscalingAddonConfiguration.from_dict(workload_autoscaling_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


