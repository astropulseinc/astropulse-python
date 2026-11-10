# OrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The organization name (required, 1-50 characters, valid DNS name). Must be unique. Format: lowercase alphanumeric and hyphens, must start with a letter. | 
**title** | **str** | A human-readable display title for the organization (optional) | [optional] 

## Example

```python
from astropulse._generated.models.organization_request import OrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRequest from a JSON string
organization_request_instance = OrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationRequest.to_json())

# convert the object into a dict
organization_request_dict = organization_request_instance.to_dict()
# create an instance of OrganizationRequest from a dict
organization_request_from_dict = OrganizationRequest.from_dict(organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


