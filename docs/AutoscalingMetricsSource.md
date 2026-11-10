# AutoscalingMetricsSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prometheus** | [**AutoscalingPrometheusSource**](AutoscalingPrometheusSource.md) | The only backend this version supports. | [optional] 

## Example

```python
from astropulse._generated.models.autoscaling_metrics_source import AutoscalingMetricsSource

# TODO update the JSON string below
json = "{}"
# create an instance of AutoscalingMetricsSource from a JSON string
autoscaling_metrics_source_instance = AutoscalingMetricsSource.from_json(json)
# print the JSON string representation of the object
print(AutoscalingMetricsSource.to_json())

# convert the object into a dict
autoscaling_metrics_source_dict = autoscaling_metrics_source_instance.to_dict()
# create an instance of AutoscalingMetricsSource from a dict
autoscaling_metrics_source_from_dict = AutoscalingMetricsSource.from_dict(autoscaling_metrics_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


