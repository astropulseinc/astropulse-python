# DeleteAPIKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from astropulse._generated.models.delete_api_key_response import DeleteAPIKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAPIKeyResponse from a JSON string
delete_api_key_response_instance = DeleteAPIKeyResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAPIKeyResponse.to_json())

# convert the object into a dict
delete_api_key_response_dict = delete_api_key_response_instance.to_dict()
# create an instance of DeleteAPIKeyResponse from a dict
delete_api_key_response_from_dict = DeleteAPIKeyResponse.from_dict(delete_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


