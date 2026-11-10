# ApplicationHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | The user-facing application name. | [optional] 
**current_version** | **str** | The Astro version currently deployed. | [optional] 
**entries** | [**List[ApplicationVersionEntry]**](ApplicationVersionEntry.md) | The deploy history, newest first. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Say what this history could not confirm, such as which versions can still be rolled back to; absent when there is nothing to say. | [optional] 
**rollback_state** | [**ApplicationRollbackState**](ApplicationRollbackState.md) | The current Astro rollback/pin state. | [optional] 
**timeline** | [**List[TimelineEvent]**](TimelineEvent.md) | Merges deploys/rollbacks and live-state drift events, newest first. | [optional] 

## Example

```python
from astropulse._generated.models.application_history import ApplicationHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationHistory from a JSON string
application_history_instance = ApplicationHistory.from_json(json)
# print the JSON string representation of the object
print(ApplicationHistory.to_json())

# convert the object into a dict
application_history_dict = application_history_instance.to_dict()
# create an instance of ApplicationHistory from a dict
application_history_from_dict = ApplicationHistory.from_dict(application_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


