# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | When the organization was created. | [optional] 
**feature_flags** | [**OrgFeatureFlags**](OrgFeatureFlags.md) | The features turned on for the organization. | [optional] 
**id** | **str** | Identifies the organization. | [optional] 
**is_default** | **bool** | True for your default organization, the one AstroPulse created when you signed up. | [optional] 
**members** | [**List[Member]**](Member.md) | The organization&#39;s members, returned only to an admin or owner and empty otherwise. A list of organizations may hold only your own entry. | [optional] 
**name** | **str** | The organization&#39;s unique name. | [optional] 
**org_namespace** | **str** | The Kubernetes namespace that holds the organization&#39;s resources. | [optional] 
**owner** | **bool** | Whether you own this organization. | [optional] 
**owner_user_id** | **str** | The user ID of this organization&#39;s owner. The organization routes return it only to an admin or owner. | [optional] 
**plan_id** | [**PlanId**](PlanId.md) | The organization&#39;s plan. | [optional] 
**roles** | [**List[Role]**](Role.md) | The organization&#39;s roles. | [optional] 
**slug** | **str** | The URL-safe form of the name. | [optional] 
**title** | **str** | The organization&#39;s display title. | [optional] 
**user_role** | [**OrganizationRole**](OrganizationRole.md) | Your role in this organization; absent when you hold none. | [optional] 

## Example

```python
from astropulse._generated.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


