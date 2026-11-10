# CurrentOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | [optional] 
**org_name** | **str** |  | [optional] 
**org_namespace** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.current_organization import CurrentOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentOrganization from a JSON string
current_organization_instance = CurrentOrganization.from_json(json)
# print the JSON string representation of the object
print(CurrentOrganization.to_json())

# convert the object into a dict
current_organization_dict = current_organization_instance.to_dict()
# create an instance of CurrentOrganization from a dict
current_organization_from_dict = CurrentOrganization.from_dict(current_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


