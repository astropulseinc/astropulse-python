# VaultLeaseReplaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | The new AWS access key ID of the IAM user whose key is stored. | [optional] 
**secret_access_key** | **str** | The new AWS access key&#39;s secret. | [optional] 
**service_account_key** | **str** | The new Google Cloud service account key, the JSON key file&#39;s contents as text. | [optional] 

## Example

```python
from astropulse._generated.models.vault_lease_replace_request import VaultLeaseReplaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VaultLeaseReplaceRequest from a JSON string
vault_lease_replace_request_instance = VaultLeaseReplaceRequest.from_json(json)
# print the JSON string representation of the object
print(VaultLeaseReplaceRequest.to_json())

# convert the object into a dict
vault_lease_replace_request_dict = vault_lease_replace_request_instance.to_dict()
# create an instance of VaultLeaseReplaceRequest from a dict
vault_lease_replace_request_from_dict = VaultLeaseReplaceRequest.from_dict(vault_lease_replace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


