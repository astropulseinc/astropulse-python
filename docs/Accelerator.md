# Accelerator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | How many devices one machine of this type carries. | [optional] 
**description** | **str** | What the device is for, in one sentence; absent for a model the catalog does not name. | [optional] 
**display_name** | **str** | The device&#39;s name as its maker writes it, such as NVIDIA L4; absent for a model the catalog does not name. | [optional] 
**kind** | [**AcceleratorKind**](AcceleratorKind.md) | The accelerator&#39;s class. | [optional] 
**memory_mi_b** | **int** | The memory on one device. | [optional] 
**model** | **str** | The normalised device name the catalog filters on: \&quot;l4\&quot;, \&quot;a100\&quot;, \&quot;mi300x\&quot;. | [optional] 
**provenance** | **str** | Empty when every populated field was reported by the provider, and ProvenanceCurated when the curated table supplied one. | [optional] 
**provider_type** | **str** | The provider&#39;s own identifier for the device, where the provider names it separately from the machine type (GCP&#39;s \&quot;nvidia-l4\&quot;). Empty where the machine type already determines it. | [optional] 
**vendor** | [**AcceleratorVendor**](AcceleratorVendor.md) | The device&#39;s maker; absent when the provider names none the catalog defines. | [optional] 

## Example

```python
from astropulse._generated.models.accelerator import Accelerator

# TODO update the JSON string below
json = "{}"
# create an instance of Accelerator from a JSON string
accelerator_instance = Accelerator.from_json(json)
# print the JSON string representation of the object
print(Accelerator.to_json())

# convert the object into a dict
accelerator_dict = accelerator_instance.to_dict()
# create an instance of Accelerator from a dict
accelerator_from_dict = Accelerator.from_dict(accelerator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


