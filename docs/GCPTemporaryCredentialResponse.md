# GCPTemporaryCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GCPTemporaryCredential**](GCPTemporaryCredential.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.gcp_temporary_credential_response import GCPTemporaryCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTemporaryCredentialResponse from a JSON string
gcp_temporary_credential_response_instance = GCPTemporaryCredentialResponse.from_json(json)
# print the JSON string representation of the object
print(GCPTemporaryCredentialResponse.to_json())

# convert the object into a dict
gcp_temporary_credential_response_dict = gcp_temporary_credential_response_instance.to_dict()
# create an instance of GCPTemporaryCredentialResponse from a dict
gcp_temporary_credential_response_from_dict = GCPTemporaryCredentialResponse.from_dict(gcp_temporary_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


