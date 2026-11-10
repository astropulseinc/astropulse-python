# TimelineEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | **str** | Who triggered a deploy/rollback event. | [optional] 
**actor_display** | **str** | The human-readable actor (name, falling back to email) resolved from Actor. Best-effort; empty when unresolved. Org-scoped, so no cross-org identity leak. | [optional] 
**at** | **str** | The RFC3339 event timestamp. | [optional] 
**health** | **str** | The live health for drift events. | [optional] 
**kind** | [**TimelineEventKind**](TimelineEventKind.md) | The event kind. | [optional] 
**summary** | **str** | A short human-readable description. | [optional] 
**sync** | **str** | The live sync status for drift events. | [optional] 
**version** | **str** | The Astro version for deploy/rollback events. | [optional] 

## Example

```python
from astropulse._generated.models.timeline_event import TimelineEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineEvent from a JSON string
timeline_event_instance = TimelineEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineEvent.to_json())

# convert the object into a dict
timeline_event_dict = timeline_event_instance.to_dict()
# create an instance of TimelineEvent from a dict
timeline_event_from_dict = TimelineEvent.from_dict(timeline_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


