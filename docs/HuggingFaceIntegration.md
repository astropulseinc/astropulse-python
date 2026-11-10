# HuggingFaceIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** | Reports whether a usable token is stored for the organization. | [optional] 
**connected_by** | **str** | The user who connected the current token. Admins only. | [optional] 
**connected_by_display** | **str** | Names that user, by name and email; empty when unknown. Admins only. | [optional] 
**message** | **str** | Says what to do when the state needs action; empty otherwise. | [optional] 
**state** | [**HuggingFaceIntegrationState**](HuggingFaceIntegrationState.md) | How the organization&#39;s token stands. A token that can&#39;t be read is used by nothing until it is revoked and connected again. | [optional] 
**token_fingerprint** | **str** | The last four characters of the stored token; empty when not connected, and omitted for callers who are not organization admins. | [optional] 
**updated_at** | **str** | When the token was last connected or rotated (RFC 3339); empty when not connected. | [optional] 
**verified_at** | **str** | When Hugging Face last accepted the token (RFC 3339). A token is stored only after Hugging Face accepts it. | [optional] 

## Example

```python
from astropulse._generated.models.hugging_face_integration import HuggingFaceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of HuggingFaceIntegration from a JSON string
hugging_face_integration_instance = HuggingFaceIntegration.from_json(json)
# print the JSON string representation of the object
print(HuggingFaceIntegration.to_json())

# convert the object into a dict
hugging_face_integration_dict = hugging_face_integration_instance.to_dict()
# create an instance of HuggingFaceIntegration from a dict
hugging_face_integration_from_dict = HuggingFaceIntegration.from_dict(hugging_face_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


