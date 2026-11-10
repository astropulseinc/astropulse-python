# SelfHostedCredentialStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Failure**](Failure.md) | Contains any error message if the request failed | [optional] 
**key_id** | **str** | Identifies the stored key without revealing it: the AWS access key ID or the GCP service account key ID. | [optional] 
**last_validated** | **datetime** | When AstroPulse last checked the stored credentials with the cloud provider, in RFC 3339. | [optional] 
**last_validation** | [**VaultValidation**](VaultValidation.md) | What that check found; omitted until one has run. | [optional] 
**message** | **str** | Says in one sentence what the status means for the cluster and what to do next. | [optional] 
**note** | **str** | Says how long the key stays valid, how to rotate it, and what revoking it here leaves in the cloud account. | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud the stored credentials are for: &#x60;aws&#x60; or &#x60;gcp&#x60;. | [optional] 
**service_account** | **str** | The GCP service account the stored key belongs to. | [optional] 
**status** | [**SelfHostedCredentialState**](SelfHostedCredentialState.md) | How the stored credentials stand. | [optional] 
**stored_at** | **datetime** | When AstroPulse stored the current key, in RFC 3339. | [optional] 
**vault_type** | **str** | The type of credential storage | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_credential_status import SelfHostedCredentialStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedCredentialStatus from a JSON string
self_hosted_credential_status_instance = SelfHostedCredentialStatus.from_json(json)
# print the JSON string representation of the object
print(SelfHostedCredentialStatus.to_json())

# convert the object into a dict
self_hosted_credential_status_dict = self_hosted_credential_status_instance.to_dict()
# create an instance of SelfHostedCredentialStatus from a dict
self_hosted_credential_status_from_dict = SelfHostedCredentialStatus.from_dict(self_hosted_credential_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


