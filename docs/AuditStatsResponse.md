# AuditStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuditStats**](AuditStats.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.audit_stats_response import AuditStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditStatsResponse from a JSON string
audit_stats_response_instance = AuditStatsResponse.from_json(json)
# print the JSON string representation of the object
print(AuditStatsResponse.to_json())

# convert the object into a dict
audit_stats_response_dict = audit_stats_response_instance.to_dict()
# create an instance of AuditStatsResponse from a dict
audit_stats_response_from_dict = AuditStatsResponse.from_dict(audit_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


