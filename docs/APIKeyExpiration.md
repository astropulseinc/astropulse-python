# APIKeyExpiration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** | The expiry timestamp. | [optional] 
**masked_key** | **str** | A non-secret display representation of the key. | [optional] 

## Example

```python
from astropulse._generated.models.api_key_expiration import APIKeyExpiration

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyExpiration from a JSON string
api_key_expiration_instance = APIKeyExpiration.from_json(json)
# print the JSON string representation of the object
print(APIKeyExpiration.to_json())

# convert the object into a dict
api_key_expiration_dict = api_key_expiration_instance.to_dict()
# create an instance of APIKeyExpiration from a dict
api_key_expiration_from_dict = APIKeyExpiration.from_dict(api_key_expiration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


