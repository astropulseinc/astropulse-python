# OrganizationOwnershipTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrganizationOwnershipTransfer**](OrganizationOwnershipTransfer.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.organization_ownership_transfer_response import OrganizationOwnershipTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationOwnershipTransferResponse from a JSON string
organization_ownership_transfer_response_instance = OrganizationOwnershipTransferResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationOwnershipTransferResponse.to_json())

# convert the object into a dict
organization_ownership_transfer_response_dict = organization_ownership_transfer_response_instance.to_dict()
# create an instance of OrganizationOwnershipTransferResponse from a dict
organization_ownership_transfer_response_from_dict = OrganizationOwnershipTransferResponse.from_dict(organization_ownership_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


