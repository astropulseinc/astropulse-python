# SetupStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_error** | **str** | The cloud provider&#39;s own error when the step failed. | [optional] 
**name** | **str** | The step&#39;s stable ID: plan, template, create, verify or store. | [optional] 
**reason** | **str** | Says what happened or what the step waits for. | [optional] 
**state** | [**SetupStepState**](SetupStepState.md) | Where the step stands. | [optional] 
**title** | **str** | Says what the step does. | [optional] 
**updated_at** | **str** | When the step last changed. | [optional] 

## Example

```python
from astropulse._generated.models.setup_step import SetupStep

# TODO update the JSON string below
json = "{}"
# create an instance of SetupStep from a JSON string
setup_step_instance = SetupStep.from_json(json)
# print the JSON string representation of the object
print(SetupStep.to_json())

# convert the object into a dict
setup_step_dict = setup_step_instance.to_dict()
# create an instance of SetupStep from a dict
setup_step_from_dict = SetupStep.from_dict(setup_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


