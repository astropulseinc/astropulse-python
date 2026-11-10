# ModelScalingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**ModelScalingSignal**](ModelScalingSignal.md) | What the replica count follows. | [optional] 
**metric_label** | **str** | The rule in a few words, such as \&quot;CPU above 80%\&quot; or \&quot;Fixed at 1 replica\&quot;. | [optional] 
**target** | **str** | The value the metric is held at; absent for fixed. | [optional] 

## Example

```python
from astropulse._generated.models.model_scaling_rule import ModelScalingRule

# TODO update the JSON string below
json = "{}"
# create an instance of ModelScalingRule from a JSON string
model_scaling_rule_instance = ModelScalingRule.from_json(json)
# print the JSON string representation of the object
print(ModelScalingRule.to_json())

# convert the object into a dict
model_scaling_rule_dict = model_scaling_rule_instance.to_dict()
# create an instance of ModelScalingRule from a dict
model_scaling_rule_from_dict = ModelScalingRule.from_dict(model_scaling_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


