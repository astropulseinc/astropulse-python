# CurrentOrganizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CurrentOrganization**](CurrentOrganization.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.current_organization_response import CurrentOrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentOrganizationResponse from a JSON string
current_organization_response_instance = CurrentOrganizationResponse.from_json(json)
# print the JSON string representation of the object
print(CurrentOrganizationResponse.to_json())

# convert the object into a dict
current_organization_response_dict = current_organization_response_instance.to_dict()
# create an instance of CurrentOrganizationResponse from a dict
current_organization_response_from_dict = CurrentOrganizationResponse.from_dict(current_organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


