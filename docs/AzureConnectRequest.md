# AzureConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The name of the cluster | 
**duration** | **str** | The duration for which the credentials are valid | [optional] 
**force_update** | **bool** | Bypasses cluster existence checks and forces reconfiguration | [optional] 
**resource_group** | **str** | The target Azure resource group | [optional] 
**subscription_id** | **str** | The target Azure subscription ID | [optional] 
**target_region** | **str** | The Azure region where resources should be created | [optional] 

## Example

```python
from astropulse._generated.models.azure_connect_request import AzureConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureConnectRequest from a JSON string
azure_connect_request_instance = AzureConnectRequest.from_json(json)
# print the JSON string representation of the object
print(AzureConnectRequest.to_json())

# convert the object into a dict
azure_connect_request_dict = azure_connect_request_instance.to_dict()
# create an instance of AzureConnectRequest from a dict
azure_connect_request_from_dict = AzureConnectRequest.from_dict(azure_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


