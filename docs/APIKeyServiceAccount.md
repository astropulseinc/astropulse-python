# APIKeyServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the service account. | [optional] 
**name** | **str** | Labels the service account. | [optional] 
**role** | [**OrganizationRole**](OrganizationRole.md) | The organization role the service account acts with. | [optional] 

## Example

```python
from astropulse._generated.models.api_key_service_account import APIKeyServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyServiceAccount from a JSON string
api_key_service_account_instance = APIKeyServiceAccount.from_json(json)
# print the JSON string representation of the object
print(APIKeyServiceAccount.to_json())

# convert the object into a dict
api_key_service_account_dict = api_key_service_account_instance.to_dict()
# create an instance of APIKeyServiceAccount from a dict
api_key_service_account_from_dict = APIKeyServiceAccount.from_dict(api_key_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


