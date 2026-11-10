# VaultRevocationCallback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | Says what the provider answered, in words safe to show. | [optional] 
**outcome** | [**VaultRevocationOutcome**](VaultRevocationOutcome.md) | What happened when AstroPulse revoked the credential at its provider. | [optional] 

## Example

```python
from astropulse._generated.models.vault_revocation_callback import VaultRevocationCallback

# TODO update the JSON string below
json = "{}"
# create an instance of VaultRevocationCallback from a JSON string
vault_revocation_callback_instance = VaultRevocationCallback.from_json(json)
# print the JSON string representation of the object
print(VaultRevocationCallback.to_json())

# convert the object into a dict
vault_revocation_callback_dict = vault_revocation_callback_instance.to_dict()
# create an instance of VaultRevocationCallback from a dict
vault_revocation_callback_from_dict = VaultRevocationCallback.from_dict(vault_revocation_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


