# VaultLeaseListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VaultLeaseList**](VaultLeaseList.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.vault_lease_list_response import VaultLeaseListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VaultLeaseListResponse from a JSON string
vault_lease_list_response_instance = VaultLeaseListResponse.from_json(json)
# print the JSON string representation of the object
print(VaultLeaseListResponse.to_json())

# convert the object into a dict
vault_lease_list_response_dict = vault_lease_list_response_instance.to_dict()
# create an instance of VaultLeaseListResponse from a dict
vault_lease_list_response_from_dict = VaultLeaseListResponse.from_dict(vault_lease_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


