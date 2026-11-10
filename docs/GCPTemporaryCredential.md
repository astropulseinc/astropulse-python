# GCPTemporaryCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The GCP access token for authentication | [optional] 
**expiration** | **str** | The expiration time for the credentials | [optional] 
**project_id** | **str** | The GCP project ID | [optional] 
**service_account_email** | **str** | The GCP service account email used for authentication | [optional] 

## Example

```python
from astropulse._generated.models.gcp_temporary_credential import GCPTemporaryCredential

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTemporaryCredential from a JSON string
gcp_temporary_credential_instance = GCPTemporaryCredential.from_json(json)
# print the JSON string representation of the object
print(GCPTemporaryCredential.to_json())

# convert the object into a dict
gcp_temporary_credential_dict = gcp_temporary_credential_instance.to_dict()
# create an instance of GCPTemporaryCredential from a dict
gcp_temporary_credential_from_dict = GCPTemporaryCredential.from_dict(gcp_temporary_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


