# HuggingFaceIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HuggingFaceIntegration**](HuggingFaceIntegration.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.hugging_face_integration_response import HuggingFaceIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HuggingFaceIntegrationResponse from a JSON string
hugging_face_integration_response_instance = HuggingFaceIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(HuggingFaceIntegrationResponse.to_json())

# convert the object into a dict
hugging_face_integration_response_dict = hugging_face_integration_response_instance.to_dict()
# create an instance of HuggingFaceIntegrationResponse from a dict
hugging_face_integration_response_from_dict = HuggingFaceIntegrationResponse.from_dict(hugging_face_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


