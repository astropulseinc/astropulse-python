# RevokeAPIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The unique identifier of the API key to revoke. This is the ID field, not the actual API key value. | 
**reason** | **str** | The reason for revoking the API key. This is optional and can be used to provide a reason for revoking the API key. | [optional] 

## Example

```python
from astropulse._generated.models.revoke_api_key_request import RevokeAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeAPIKeyRequest from a JSON string
revoke_api_key_request_instance = RevokeAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeAPIKeyRequest.to_json())

# convert the object into a dict
revoke_api_key_request_dict = revoke_api_key_request_instance.to_dict()
# create an instance of RevokeAPIKeyRequest from a dict
revoke_api_key_request_from_dict = RevokeAPIKeyRequest.from_dict(revoke_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


