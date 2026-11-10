# AzureTemporaryCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AzureTemporaryCredential**](AzureTemporaryCredential.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.azure_temporary_credential_response import AzureTemporaryCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTemporaryCredentialResponse from a JSON string
azure_temporary_credential_response_instance = AzureTemporaryCredentialResponse.from_json(json)
# print the JSON string representation of the object
print(AzureTemporaryCredentialResponse.to_json())

# convert the object into a dict
azure_temporary_credential_response_dict = azure_temporary_credential_response_instance.to_dict()
# create an instance of AzureTemporaryCredentialResponse from a dict
azure_temporary_credential_response_from_dict = AzureTemporaryCredentialResponse.from_dict(azure_temporary_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


