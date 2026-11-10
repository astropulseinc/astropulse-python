# VaultValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | Says why, in words safe to show; never part of the credential. | [optional] 
**result** | [**VaultValidationResult**](VaultValidationResult.md) | Whether the provider accepted the credential. | [optional] 

## Example

```python
from astropulse._generated.models.vault_validation import VaultValidation

# TODO update the JSON string below
json = "{}"
# create an instance of VaultValidation from a JSON string
vault_validation_instance = VaultValidation.from_json(json)
# print the JSON string representation of the object
print(VaultValidation.to_json())

# convert the object into a dict
vault_validation_dict = vault_validation_instance.to_dict()
# create an instance of VaultValidation from a dict
vault_validation_from_dict = VaultValidation.from_dict(vault_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


