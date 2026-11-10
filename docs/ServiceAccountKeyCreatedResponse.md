# ServiceAccountKeyCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceAccountKeyCreated**](ServiceAccountKeyCreated.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.service_account_key_created_response import ServiceAccountKeyCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountKeyCreatedResponse from a JSON string
service_account_key_created_response_instance = ServiceAccountKeyCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountKeyCreatedResponse.to_json())

# convert the object into a dict
service_account_key_created_response_dict = service_account_key_created_response_instance.to_dict()
# create an instance of ServiceAccountKeyCreatedResponse from a dict
service_account_key_created_response_from_dict = ServiceAccountKeyCreatedResponse.from_dict(service_account_key_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


