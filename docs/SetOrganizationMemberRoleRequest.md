# SetOrganizationMemberRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**OrganizationRole**](OrganizationRole.md) | The member&#39;s new role. Only the organization owner can grant or take away admin, and the owner&#39;s own role never changes. | 

## Example

```python
from astropulse._generated.models.set_organization_member_role_request import SetOrganizationMemberRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetOrganizationMemberRoleRequest from a JSON string
set_organization_member_role_request_instance = SetOrganizationMemberRoleRequest.from_json(json)
# print the JSON string representation of the object
print(SetOrganizationMemberRoleRequest.to_json())

# convert the object into a dict
set_organization_member_role_request_dict = set_organization_member_role_request_instance.to_dict()
# create an instance of SetOrganizationMemberRoleRequest from a dict
set_organization_member_role_request_from_dict = SetOrganizationMemberRoleRequest.from_dict(set_organization_member_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


