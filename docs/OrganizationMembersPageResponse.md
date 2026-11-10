# OrganizationMembersPageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrganizationMembersPage**](OrganizationMembersPage.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.organization_members_page_response import OrganizationMembersPageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMembersPageResponse from a JSON string
organization_members_page_response_instance = OrganizationMembersPageResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationMembersPageResponse.to_json())

# convert the object into a dict
organization_members_page_response_dict = organization_members_page_response_instance.to_dict()
# create an instance of OrganizationMembersPageResponse from a dict
organization_members_page_response_from_dict = OrganizationMembersPageResponse.from_dict(organization_members_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


