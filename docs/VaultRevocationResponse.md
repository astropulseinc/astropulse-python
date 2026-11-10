# VaultRevocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VaultRevocation**](VaultRevocation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.vault_revocation_response import VaultRevocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VaultRevocationResponse from a JSON string
vault_revocation_response_instance = VaultRevocationResponse.from_json(json)
# print the JSON string representation of the object
print(VaultRevocationResponse.to_json())

# convert the object into a dict
vault_revocation_response_dict = vault_revocation_response_instance.to_dict()
# create an instance of VaultRevocationResponse from a dict
vault_revocation_response_from_dict = VaultRevocationResponse.from_dict(vault_revocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


