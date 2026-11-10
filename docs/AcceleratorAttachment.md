# AcceleratorAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu** | [**GPUAttachment**](GPUAttachment.md) | Requests GPU hardware by normalized identity. | [optional] 

## Example

```python
from astropulse._generated.models.accelerator_attachment import AcceleratorAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of AcceleratorAttachment from a JSON string
accelerator_attachment_instance = AcceleratorAttachment.from_json(json)
# print the JSON string representation of the object
print(AcceleratorAttachment.to_json())

# convert the object into a dict
accelerator_attachment_dict = accelerator_attachment_instance.to_dict()
# create an instance of AcceleratorAttachment from a dict
accelerator_attachment_from_dict = AcceleratorAttachment.from_dict(accelerator_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


