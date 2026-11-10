# ModelGPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_type** | [**ModelCapacityType**](ModelCapacityType.md) | How a replica&#39;s GPU node is bought. | [optional] 
**count_per_replica** | **int** | How many devices one replica needs. | [optional] 
**model** | **str** | The normalized GPU model (l4, a10g, a100, h100, ...), as the machine catalog names it. | [optional] 
**vendor** | **str** | Narrows the GPU vendor (nvidia, amd). Optional when model already identifies the hardware. | [optional] 

## Example

```python
from astropulse._generated.models.model_gpu import ModelGPU

# TODO update the JSON string below
json = "{}"
# create an instance of ModelGPU from a JSON string
model_gpu_instance = ModelGPU.from_json(json)
# print the JSON string representation of the object
print(ModelGPU.to_json())

# convert the object into a dict
model_gpu_dict = model_gpu_instance.to_dict()
# create an instance of ModelGPU from a dict
model_gpu_from_dict = ModelGPU.from_dict(model_gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


