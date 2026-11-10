# OrgServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived_at** | **str** | When the account was archived. An archived account and all its keys are disabled permanently. | [optional] 
**created_at** | **str** | The creation timestamp. | [optional] 
**created_by** | **str** | Identifies the user who created this account. | [optional] 
**description** | **str** | Describes the automation. | [optional] 
**id** | **str** | Identifies this service account. | [optional] 
**name** | **str** | Labels this service account. | [optional] 
**org_id** | **str** | Identifies the owning organization. | [optional] 
**role** | [**OrganizationRole**](OrganizationRole.md) | The organization&#39;s role assigned to this account. | [optional] 

## Example

```python
from astropulse._generated.models.org_service_account import OrgServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of OrgServiceAccount from a JSON string
org_service_account_instance = OrgServiceAccount.from_json(json)
# print the JSON string representation of the object
print(OrgServiceAccount.to_json())

# convert the object into a dict
org_service_account_dict = org_service_account_instance.to_dict()
# create an instance of OrgServiceAccount from a dict
org_service_account_from_dict = OrgServiceAccount.from_dict(org_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


