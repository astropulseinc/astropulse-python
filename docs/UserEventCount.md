# UserEventCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_count** | **int** | The number of events for this user | [optional] 
**name** | **str** | The display name of the user | [optional] 
**user_id** | **str** | The unique identifier of the user | [optional] 

## Example

```python
from astropulse._generated.models.user_event_count import UserEventCount

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventCount from a JSON string
user_event_count_instance = UserEventCount.from_json(json)
# print the JSON string representation of the object
print(UserEventCount.to_json())

# convert the object into a dict
user_event_count_dict = user_event_count_instance.to_dict()
# create an instance of UserEventCount from a dict
user_event_count_from_dict = UserEventCount.from_dict(user_event_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


