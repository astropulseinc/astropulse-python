# SelfHostedCredentialRevocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** | Whether stored credentials were found and deleted. | [optional] 
**message** | **str** | Says what was deleted and which key is still valid in the cloud account. | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_credential_revocation import SelfHostedCredentialRevocation

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedCredentialRevocation from a JSON string
self_hosted_credential_revocation_instance = SelfHostedCredentialRevocation.from_json(json)
# print the JSON string representation of the object
print(SelfHostedCredentialRevocation.to_json())

# convert the object into a dict
self_hosted_credential_revocation_dict = self_hosted_credential_revocation_instance.to_dict()
# create an instance of SelfHostedCredentialRevocation from a dict
self_hosted_credential_revocation_from_dict = SelfHostedCredentialRevocation.from_dict(self_hosted_credential_revocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


