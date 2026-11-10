# ModelScaling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_replicas** | **int** | The ceiling. Defaults to minReplicas, or 1. Equal to minReplicas, the model runs at that fixed count with no autoscaler. | [optional] 
**metric** | [**ModelScalingMetric**](ModelScalingMetric.md) | The signal replicas follow, and needs maxReplicas above minReplicas. Left unset, AstroPulse chooses the one that suits the model. | [optional] 
**min_replicas** | **int** | The floor, at least 1. Scaling to zero is not supported: it needs a request-driven wake-up path in front of the predictor, and without one a model at zero replicas never comes back. | [optional] 

## Example

```python
from astropulse._generated.models.model_scaling import ModelScaling

# TODO update the JSON string below
json = "{}"
# create an instance of ModelScaling from a JSON string
model_scaling_instance = ModelScaling.from_json(json)
# print the JSON string representation of the object
print(ModelScaling.to_json())

# convert the object into a dict
model_scaling_dict = model_scaling_instance.to_dict()
# create an instance of ModelScaling from a dict
model_scaling_from_dict = ModelScaling.from_dict(model_scaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


