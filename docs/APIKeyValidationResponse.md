# APIKeyValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**APIKeyValidation**](APIKeyValidation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.api_key_validation_response import APIKeyValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyValidationResponse from a JSON string
api_key_validation_response_instance = APIKeyValidationResponse.from_json(json)
# print the JSON string representation of the object
print(APIKeyValidationResponse.to_json())

# convert the object into a dict
api_key_validation_response_dict = api_key_validation_response_instance.to_dict()
# create an instance of APIKeyValidationResponse from a dict
api_key_validation_response_from_dict = APIKeyValidationResponse.from_dict(api_key_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


