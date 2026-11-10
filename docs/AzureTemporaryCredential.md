# AzureTemporaryCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The Azure access token for cluster API authentication | [optional] 
**aks_api_audience** | **str** | The token audience scoped to the AKS cluster API | [optional] 
**client_id** | **str** | The Azure application client ID | [optional] 
**expiration** | **str** | The expiration time for the credentials | [optional] 
**resource_group** | **str** | The Azure resource group | [optional] 
**subscription_id** | **str** | The Azure subscription ID | [optional] 

## Example

```python
from astropulse._generated.models.azure_temporary_credential import AzureTemporaryCredential

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTemporaryCredential from a JSON string
azure_temporary_credential_instance = AzureTemporaryCredential.from_json(json)
# print the JSON string representation of the object
print(AzureTemporaryCredential.to_json())

# convert the object into a dict
azure_temporary_credential_dict = azure_temporary_credential_instance.to_dict()
# create an instance of AzureTemporaryCredential from a dict
azure_temporary_credential_from_dict = AzureTemporaryCredential.from_dict(azure_temporary_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


