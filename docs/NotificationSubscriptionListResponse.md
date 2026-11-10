# NotificationSubscriptionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NotificationSubscription]**](NotificationSubscription.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.notification_subscription_list_response import NotificationSubscriptionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubscriptionListResponse from a JSON string
notification_subscription_list_response_instance = NotificationSubscriptionListResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationSubscriptionListResponse.to_json())

# convert the object into a dict
notification_subscription_list_response_dict = notification_subscription_list_response_instance.to_dict()
# create an instance of NotificationSubscriptionListResponse from a dict
notification_subscription_list_response_from_dict = NotificationSubscriptionListResponse.from_dict(notification_subscription_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


