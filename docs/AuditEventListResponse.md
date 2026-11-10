# AuditEventListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuditEventList**](AuditEventList.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.audit_event_list_response import AuditEventListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEventListResponse from a JSON string
audit_event_list_response_instance = AuditEventListResponse.from_json(json)
# print the JSON string representation of the object
print(AuditEventListResponse.to_json())

# convert the object into a dict
audit_event_list_response_dict = audit_event_list_response_instance.to_dict()
# create an instance of AuditEventListResponse from a dict
audit_event_list_response_from_dict = AuditEventListResponse.from_dict(audit_event_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


