# OrganizationOwnershipTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_owner_user_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**previous_owner_user_id** | **str** | Stays a member of the organization as admin. | [optional] 

## Example

```python
from astropulse._generated.models.organization_ownership_transfer import OrganizationOwnershipTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationOwnershipTransfer from a JSON string
organization_ownership_transfer_instance = OrganizationOwnershipTransfer.from_json(json)
# print the JSON string representation of the object
print(OrganizationOwnershipTransfer.to_json())

# convert the object into a dict
organization_ownership_transfer_dict = organization_ownership_transfer_instance.to_dict()
# create an instance of OrganizationOwnershipTransfer from a dict
organization_ownership_transfer_from_dict = OrganizationOwnershipTransfer.from_dict(organization_ownership_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


