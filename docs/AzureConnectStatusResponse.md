# AzureConnectStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AzureConnectStatus**](AzureConnectStatus.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.azure_connect_status_response import AzureConnectStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AzureConnectStatusResponse from a JSON string
azure_connect_status_response_instance = AzureConnectStatusResponse.from_json(json)
# print the JSON string representation of the object
print(AzureConnectStatusResponse.to_json())

# convert the object into a dict
azure_connect_status_response_dict = azure_connect_status_response_instance.to_dict()
# create an instance of AzureConnectStatusResponse from a dict
azure_connect_status_response_from_dict = AzureConnectStatusResponse.from_dict(azure_connect_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


