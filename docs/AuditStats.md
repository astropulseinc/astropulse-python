# AuditStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_by_action** | **Dict[str, int]** | Counts events per action, keyed by the action, such as Create. | [optional] 
**events_by_type** | **Dict[str, int]** | Counts events per event type, keyed by the event type, such as Cluster. | [optional] 
**org_id** | **str** | The organization these statistics are for | [optional] 
**period** | **str** | Indicates the time period for these statistics (7d, 30d, 90d) | [optional] 
**top_users** | [**List[UserEventCount]**](UserEventCount.md) | Lists the users with the most audit events | [optional] 
**total_events** | **int** | The total number of audit events in the specified period | [optional] 

## Example

```python
from astropulse._generated.models.audit_stats import AuditStats

# TODO update the JSON string below
json = "{}"
# create an instance of AuditStats from a JSON string
audit_stats_instance = AuditStats.from_json(json)
# print the JSON string representation of the object
print(AuditStats.to_json())

# convert the object into a dict
audit_stats_dict = audit_stats_instance.to_dict()
# create an instance of AuditStats from a dict
audit_stats_from_dict = AuditStats.from_dict(audit_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


