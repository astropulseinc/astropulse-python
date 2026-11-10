# MetricsDimensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_cpu_cores_used** | **float** | The CPU used across the reading. | [optional] 
**memory_working_set_bytes** | **float** | The memory held across it. | [optional] 
**network_receive_bytes_per_second** | **float** | The network receive and transmit rates are absent (not zero) unless every sample contributing to this reading carried a network measurement — never present when any contributor&#39;s source was metrics-api, and never present at cluster scope unless every reporting application observed network. A zero here would read as \&quot;no traffic,\&quot; which looks exactly like an outage. | [optional] 
**network_transmit_bytes_per_second** | **float** |  | [optional] 

## Example

```python
from astropulse._generated.models.metrics_dimensions import MetricsDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsDimensions from a JSON string
metrics_dimensions_instance = MetricsDimensions.from_json(json)
# print the JSON string representation of the object
print(MetricsDimensions.to_json())

# convert the object into a dict
metrics_dimensions_dict = metrics_dimensions_instance.to_dict()
# create an instance of MetricsDimensions from a dict
metrics_dimensions_from_dict = MetricsDimensions.from_dict(metrics_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


