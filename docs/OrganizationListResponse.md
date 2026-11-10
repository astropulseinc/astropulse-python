# OrganizationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Organization]**](Organization.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.organization_list_response import OrganizationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationListResponse from a JSON string
organization_list_response_instance = OrganizationListResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationListResponse.to_json())

# convert the object into a dict
organization_list_response_dict = organization_list_response_instance.to_dict()
# create an instance of OrganizationListResponse from a dict
organization_list_response_from_dict = OrganizationListResponse.from_dict(organization_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


