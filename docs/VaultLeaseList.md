# VaultLeaseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leases** | [**List[VaultLease]**](VaultLease.md) | This page, oldest first. | [optional] 
**next_page_token** | **str** | Fetches the next page; empty on the last one. | [optional] 

## Example

```python
from astropulse._generated.models.vault_lease_list import VaultLeaseList

# TODO update the JSON string below
json = "{}"
# create an instance of VaultLeaseList from a JSON string
vault_lease_list_instance = VaultLeaseList.from_json(json)
# print the JSON string representation of the object
print(VaultLeaseList.to_json())

# convert the object into a dict
vault_lease_list_dict = vault_lease_list_instance.to_dict()
# create an instance of VaultLeaseList from a dict
vault_lease_list_from_dict = VaultLeaseList.from_dict(vault_lease_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


