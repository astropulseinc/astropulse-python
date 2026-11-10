# DeleteAPIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The unique identifier of the API key to delete. This is the ID field, not the actual API key value. | 

## Example

```python
from astropulse._generated.models.delete_api_key_request import DeleteAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAPIKeyRequest from a JSON string
delete_api_key_request_instance = DeleteAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteAPIKeyRequest.to_json())

# convert the object into a dict
delete_api_key_request_dict = delete_api_key_request_instance.to_dict()
# create an instance of DeleteAPIKeyRequest from a dict
delete_api_key_request_from_dict = DeleteAPIKeyRequest.from_dict(delete_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


