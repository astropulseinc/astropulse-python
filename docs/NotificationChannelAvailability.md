# NotificationChannelAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**NotificationChannelType**](NotificationChannelType.md) | The delivery channel. | [optional] 
**current_plan** | **str** | The organization&#39;s plan. | [optional] 
**included_in_plan** | **bool** | True when the organization&#39;s plan includes the channel. | [optional] 
**notice** | [**Notice**](Notice.md) | Says which plan includes the channel and how to upgrade to it; absent when the current plan includes it. | [optional] 
**required_plan** | **str** | The plan that includes the channel, set when the current plan does not. | [optional] 

## Example

```python
from astropulse._generated.models.notification_channel_availability import NotificationChannelAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelAvailability from a JSON string
notification_channel_availability_instance = NotificationChannelAvailability.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelAvailability.to_json())

# convert the object into a dict
notification_channel_availability_dict = notification_channel_availability_instance.to_dict()
# create an instance of NotificationChannelAvailability from a dict
notification_channel_availability_from_dict = NotificationChannelAvailability.from_dict(notification_channel_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


