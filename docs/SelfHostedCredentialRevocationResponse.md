# SelfHostedCredentialRevocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SelfHostedCredentialRevocation**](SelfHostedCredentialRevocation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_credential_revocation_response import SelfHostedCredentialRevocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedCredentialRevocationResponse from a JSON string
self_hosted_credential_revocation_response_instance = SelfHostedCredentialRevocationResponse.from_json(json)
# print the JSON string representation of the object
print(SelfHostedCredentialRevocationResponse.to_json())

# convert the object into a dict
self_hosted_credential_revocation_response_dict = self_hosted_credential_revocation_response_instance.to_dict()
# create an instance of SelfHostedCredentialRevocationResponse from a dict
self_hosted_credential_revocation_response_from_dict = SelfHostedCredentialRevocationResponse.from_dict(self_hosted_credential_revocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


