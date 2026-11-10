# ModelRuntimeChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The model format it serves the model as, for example vllm. | [optional] 
**name** | **str** | The serving runtime, for example kserve-vllm. | [optional] 
**pinned** | **bool** | True when the request named the runtime (model.runtime.engine) and false when it was chosen from the format. | [optional] 
**summary** | **str** | Says in one sentence which runtime the model runs on and why. | [optional] 

## Example

```python
from astropulse._generated.models.model_runtime_choice import ModelRuntimeChoice

# TODO update the JSON string below
json = "{}"
# create an instance of ModelRuntimeChoice from a JSON string
model_runtime_choice_instance = ModelRuntimeChoice.from_json(json)
# print the JSON string representation of the object
print(ModelRuntimeChoice.to_json())

# convert the object into a dict
model_runtime_choice_dict = model_runtime_choice_instance.to_dict()
# create an instance of ModelRuntimeChoice from a dict
model_runtime_choice_from_dict = ModelRuntimeChoice.from_dict(model_runtime_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


