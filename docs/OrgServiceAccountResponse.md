# OrgServiceAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrgServiceAccount**](OrgServiceAccount.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.org_service_account_response import OrgServiceAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgServiceAccountResponse from a JSON string
org_service_account_response_instance = OrgServiceAccountResponse.from_json(json)
# print the JSON string representation of the object
print(OrgServiceAccountResponse.to_json())

# convert the object into a dict
org_service_account_response_dict = org_service_account_response_instance.to_dict()
# create an instance of OrgServiceAccountResponse from a dict
org_service_account_response_from_dict = OrgServiceAccountResponse.from_dict(org_service_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


