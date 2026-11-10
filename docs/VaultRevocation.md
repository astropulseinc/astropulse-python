# VaultRevocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | [**VaultRevocationCallback**](VaultRevocationCallback.md) | What happened at the provider, for kinds that revoke the credential there too. | [optional] 
**lease** | [**VaultLease**](VaultLease.md) | The credential that was revoked. | [optional] 
**stops_working** | **str** | Says what no longer works now the credential is gone. | [optional] 

## Example

```python
from astropulse._generated.models.vault_revocation import VaultRevocation

# TODO update the JSON string below
json = "{}"
# create an instance of VaultRevocation from a JSON string
vault_revocation_instance = VaultRevocation.from_json(json)
# print the JSON string representation of the object
print(VaultRevocation.to_json())

# convert the object into a dict
vault_revocation_dict = vault_revocation_instance.to_dict()
# create an instance of VaultRevocation from a dict
vault_revocation_from_dict = VaultRevocation.from_dict(vault_revocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


