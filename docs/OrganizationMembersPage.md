# OrganizationMembersPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Continues the listing when passed back as pageToken; empty on the last page. | [optional] 
**pagination** | [**Pagination**](Pagination.md) | Where this page is in the whole list. | [optional] 
**users** | [**List[OrganizationMember]**](OrganizationMember.md) | The members on this page. | [optional] 

## Example

```python
from astropulse._generated.models.organization_members_page import OrganizationMembersPage

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMembersPage from a JSON string
organization_members_page_instance = OrganizationMembersPage.from_json(json)
# print the JSON string representation of the object
print(OrganizationMembersPage.to_json())

# convert the object into a dict
organization_members_page_dict = organization_members_page_instance.to_dict()
# create an instance of OrganizationMembersPage from a dict
organization_members_page_from_dict = OrganizationMembersPage.from_dict(organization_members_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


