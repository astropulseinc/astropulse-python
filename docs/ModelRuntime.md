# ModelRuntime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | The serving runtime, by its short name (vllm, triton, sklearn, xgboost, lightgbm, tensorflow, torchserve, mlserver) or the full ClusterServingRuntime name. | [optional] 

## Example

```python
from astropulse._generated.models.model_runtime import ModelRuntime

# TODO update the JSON string below
json = "{}"
# create an instance of ModelRuntime from a JSON string
model_runtime_instance = ModelRuntime.from_json(json)
# print the JSON string representation of the object
print(ModelRuntime.to_json())

# convert the object into a dict
model_runtime_dict = model_runtime_instance.to_dict()
# create an instance of ModelRuntime from a dict
model_runtime_from_dict = ModelRuntime.from_dict(model_runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


