# ModelScalingMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**ModelScalingTarget**](ModelScalingTarget.md) | Scales on CPU utilisation percent, through a plain HorizontalPodAutoscaler. Right for a predictive model, where CPU is the work. | [optional] 
**requests_waiting** | [**ModelScalingTarget**](ModelScalingTarget.md) | Scales on requests waiting to be scheduled, through KEDA. Right for a generative model: it rises before users wait. | [optional] 

## Example

```python
from astropulse._generated.models.model_scaling_metric import ModelScalingMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ModelScalingMetric from a JSON string
model_scaling_metric_instance = ModelScalingMetric.from_json(json)
# print the JSON string representation of the object
print(ModelScalingMetric.to_json())

# convert the object into a dict
model_scaling_metric_dict = model_scaling_metric_instance.to_dict()
# create an instance of ModelScalingMetric from a dict
model_scaling_metric_from_dict = ModelScalingMetric.from_dict(model_scaling_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


