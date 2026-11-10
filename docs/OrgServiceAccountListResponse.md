# OrgServiceAccountListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OrgServiceAccount]**](OrgServiceAccount.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.org_service_account_list_response import OrgServiceAccountListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgServiceAccountListResponse from a JSON string
org_service_account_list_response_instance = OrgServiceAccountListResponse.from_json(json)
# print the JSON string representation of the object
print(OrgServiceAccountListResponse.to_json())

# convert the object into a dict
org_service_account_list_response_dict = org_service_account_list_response_instance.to_dict()
# create an instance of OrgServiceAccountListResponse from a dict
org_service_account_list_response_from_dict = OrgServiceAccountListResponse.from_dict(org_service_account_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


