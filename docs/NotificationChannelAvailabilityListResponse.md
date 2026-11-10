# NotificationChannelAvailabilityListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NotificationChannelAvailability]**](NotificationChannelAvailability.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.notification_channel_availability_list_response import NotificationChannelAvailabilityListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelAvailabilityListResponse from a JSON string
notification_channel_availability_list_response_instance = NotificationChannelAvailabilityListResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelAvailabilityListResponse.to_json())

# convert the object into a dict
notification_channel_availability_list_response_dict = notification_channel_availability_list_response_instance.to_dict()
# create an instance of NotificationChannelAvailabilityListResponse from a dict
notification_channel_availability_list_response_from_dict = NotificationChannelAvailabilityListResponse.from_dict(notification_channel_availability_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


