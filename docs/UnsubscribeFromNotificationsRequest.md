# UnsubscribeFromNotificationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**NotificationChannelType**](NotificationChannelType.md) | The optional notification channel to unsubscribe from If not specified, unsubscribes from all channels for the topic | [optional] 
**topic** | [**NotificationTopic**](NotificationTopic.md) | The notification topic to unsubscribe from. | 

## Example

```python
from astropulse._generated.models.unsubscribe_from_notifications_request import UnsubscribeFromNotificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnsubscribeFromNotificationsRequest from a JSON string
unsubscribe_from_notifications_request_instance = UnsubscribeFromNotificationsRequest.from_json(json)
# print the JSON string representation of the object
print(UnsubscribeFromNotificationsRequest.to_json())

# convert the object into a dict
unsubscribe_from_notifications_request_dict = unsubscribe_from_notifications_request_instance.to_dict()
# create an instance of UnsubscribeFromNotificationsRequest from a dict
unsubscribe_from_notifications_request_from_dict = UnsubscribeFromNotificationsRequest.from_dict(unsubscribe_from_notifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


