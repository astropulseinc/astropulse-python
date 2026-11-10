# RemoveUserFromOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | The organization identifier (required, UUID format) | 
**user_id** | **str** | The user identifier (required, UUID format) | 

## Example

```python
from astropulse._generated.models.remove_user_from_organization_request import RemoveUserFromOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserFromOrganizationRequest from a JSON string
remove_user_from_organization_request_instance = RemoveUserFromOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveUserFromOrganizationRequest.to_json())

# convert the object into a dict
remove_user_from_organization_request_dict = remove_user_from_organization_request_instance.to_dict()
# create an instance of RemoveUserFromOrganizationRequest from a dict
remove_user_from_organization_request_from_dict = RemoveUserFromOrganizationRequest.from_dict(remove_user_from_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


