# TransferOrganizationOwnershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The new owner: a member of the organization holding the global admin role. | 

## Example

```python
from astropulse._generated.models.transfer_organization_ownership_request import TransferOrganizationOwnershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOrganizationOwnershipRequest from a JSON string
transfer_organization_ownership_request_instance = TransferOrganizationOwnershipRequest.from_json(json)
# print the JSON string representation of the object
print(TransferOrganizationOwnershipRequest.to_json())

# convert the object into a dict
transfer_organization_ownership_request_dict = transfer_organization_ownership_request_instance.to_dict()
# create an instance of TransferOrganizationOwnershipRequest from a dict
transfer_organization_ownership_request_from_dict = TransferOrganizationOwnershipRequest.from_dict(transfer_organization_ownership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


