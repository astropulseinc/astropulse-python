# ModelAccelerator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu** | [**ModelGPU**](ModelGPU.md) | Requests GPUs. | [optional] 

## Example

```python
from astropulse._generated.models.model_accelerator import ModelAccelerator

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccelerator from a JSON string
model_accelerator_instance = ModelAccelerator.from_json(json)
# print the JSON string representation of the object
print(ModelAccelerator.to_json())

# convert the object into a dict
model_accelerator_dict = model_accelerator_instance.to_dict()
# create an instance of ModelAccelerator from a dict
model_accelerator_from_dict = ModelAccelerator.from_dict(model_accelerator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


