# GPUAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_per_node** | **int** | How many devices each node carries (required, &gt;&#x3D; 1). The accelerator catalog lists the valid counts for a given model in its countsPerNode field. | [optional] 
**model** | **str** | The required normalized model (e.g. \&quot;l4\&quot;, \&quot;a100\&quot;, \&quot;mi300x\&quot;) — exactly the vocabulary the machine catalog and its filters use. | 
**provider_type** | **str** | The provider-native accelerator identifier AstroPulse RESOLVED for this attachment (GCP&#39;s guestAccelerator type, e.g. \&quot;nvidia-l4\&quot;); empty on providers whose machine type already determines the device (AWS, Azure). Read-only: it is a plan output recorded for auditability, never user input — a value sent on create or update is ignored and re-resolved from the catalog. | [optional] [readonly] 
**vendor** | [**AcceleratorVendor**](AcceleratorVendor.md) | The device&#39;s maker, for when the model alone is ambiguous. | [optional] 

## Example

```python
from astropulse._generated.models.gpu_attachment import GPUAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of GPUAttachment from a JSON string
gpu_attachment_instance = GPUAttachment.from_json(json)
# print the JSON string representation of the object
print(GPUAttachment.to_json())

# convert the object into a dict
gpu_attachment_dict = gpu_attachment_instance.to_dict()
# create an instance of GPUAttachment from a dict
gpu_attachment_from_dict = GPUAttachment.from_dict(gpu_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


