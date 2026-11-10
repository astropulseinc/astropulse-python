# NotificationSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[NotificationChannelType]**](NotificationChannelType.md) | The channels to deliver notifications on the topic through; at least one. | [optional] 
**enabled** | **bool** | Whether notifications on the topic are delivered. | [optional] 
**topic** | [**NotificationTopic**](NotificationTopic.md) | The notification topic. | [optional] 

## Example

```python
from astropulse._generated.models.notification_subscription_request import NotificationSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubscriptionRequest from a JSON string
notification_subscription_request_instance = NotificationSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationSubscriptionRequest.to_json())

# convert the object into a dict
notification_subscription_request_dict = notification_subscription_request_instance.to_dict()
# create an instance of NotificationSubscriptionRequest from a dict
notification_subscription_request_from_dict = NotificationSubscriptionRequest.from_dict(notification_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


