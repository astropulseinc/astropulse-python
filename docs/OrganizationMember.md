# OrganizationMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The member&#39;s email address. | [optional] 
**joined_at** | **str** | When the member joined the organization. | [optional] 
**name** | **str** | The member&#39;s name. | [optional] 
**org_id** | **str** | The organization&#39;s ID. | [optional] 
**plan_id** | [**PlanId**](PlanId.md) | The organization&#39;s plan. | [optional] 
**role** | [**OrganizationRole**](OrganizationRole.md) | The member&#39;s role in the organization. | [optional] 
**user_id** | **str** | The member&#39;s user ID. | [optional] 

## Example

```python
from astropulse._generated.models.organization_member import OrganizationMember

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMember from a JSON string
organization_member_instance = OrganizationMember.from_json(json)
# print the JSON string representation of the object
print(OrganizationMember.to_json())

# convert the object into a dict
organization_member_dict = organization_member_instance.to_dict()
# create an instance of OrganizationMember from a dict
organization_member_from_dict = OrganizationMember.from_dict(organization_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


