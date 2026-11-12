# AutoscalingPrometheusSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | The address of a Prometheus, reachable from the cluster, that already collects the scaled workloads&#39; metrics labelled by &#x60;namespace&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.autoscaling_prometheus_source import AutoscalingPrometheusSource

# TODO update the JSON string below
json = "{}"
# create an instance of AutoscalingPrometheusSource from a JSON string
autoscaling_prometheus_source_instance = AutoscalingPrometheusSource.from_json(json)
# print the JSON string representation of the object
print(AutoscalingPrometheusSource.to_json())

# convert the object into a dict
autoscaling_prometheus_source_dict = autoscaling_prometheus_source_instance.to_dict()
# create an instance of AutoscalingPrometheusSource from a dict
autoscaling_prometheus_source_from_dict = AutoscalingPrometheusSource.from_dict(autoscaling_prometheus_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


