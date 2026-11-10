# NotificationSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NotificationSubscription**](NotificationSubscription.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.notification_subscription_response import NotificationSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubscriptionResponse from a JSON string
notification_subscription_response_instance = NotificationSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationSubscriptionResponse.to_json())

# convert the object into a dict
notification_subscription_response_dict = notification_subscription_response_instance.to_dict()
# create an instance of NotificationSubscriptionResponse from a dict
notification_subscription_response_from_dict = NotificationSubscriptionResponse.from_dict(notification_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


