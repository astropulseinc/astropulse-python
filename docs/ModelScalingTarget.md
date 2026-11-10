# ModelScalingTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | The figure replicas are added to defend: a utilisation percent for cpu (\&quot;60\&quot;), a number of waiting requests for requestsWaiting (\&quot;2\&quot;). | [optional] 

## Example

```python
from astropulse._generated.models.model_scaling_target import ModelScalingTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ModelScalingTarget from a JSON string
model_scaling_target_instance = ModelScalingTarget.from_json(json)
# print the JSON string representation of the object
print(ModelScalingTarget.to_json())

# convert the object into a dict
model_scaling_target_dict = model_scaling_target_instance.to_dict()
# create an instance of ModelScalingTarget from a dict
model_scaling_target_from_dict = ModelScalingTarget.from_dict(model_scaling_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


