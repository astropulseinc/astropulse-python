# AuditEventList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AuditEvent]**](AuditEvent.md) | The list of audit events for the current page | [optional] 
**next_page_token** | **str** | Continues the listing when passed back as pageToken; empty on the last page. | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Contains pagination metadata | [optional] 

## Example

```python
from astropulse._generated.models.audit_event_list import AuditEventList

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEventList from a JSON string
audit_event_list_instance = AuditEventList.from_json(json)
# print the JSON string representation of the object
print(AuditEventList.to_json())

# convert the object into a dict
audit_event_list_dict = audit_event_list_instance.to_dict()
# create an instance of AuditEventList from a dict
audit_event_list_from_dict = AuditEventList.from_dict(audit_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


