# HuggingFaceIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | A Hugging Face user access token (starts with hf_). A read-only token is all AstroPulse needs. | 

## Example

```python
from astropulse._generated.models.hugging_face_integration_request import HuggingFaceIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HuggingFaceIntegrationRequest from a JSON string
hugging_face_integration_request_instance = HuggingFaceIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(HuggingFaceIntegrationRequest.to_json())

# convert the object into a dict
hugging_face_integration_request_dict = hugging_face_integration_request_instance.to_dict()
# create an instance of HuggingFaceIntegrationRequest from a dict
hugging_face_integration_request_from_dict = HuggingFaceIntegrationRequest.from_dict(hugging_face_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


