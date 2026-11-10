# APIKeyCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**APIKeyCreated**](APIKeyCreated.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.api_key_created_response import APIKeyCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyCreatedResponse from a JSON string
api_key_created_response_instance = APIKeyCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(APIKeyCreatedResponse.to_json())

# convert the object into a dict
api_key_created_response_dict = api_key_created_response_instance.to_dict()
# create an instance of APIKeyCreatedResponse from a dict
api_key_created_response_from_dict = APIKeyCreatedResponse.from_dict(api_key_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


