# NotificationSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[NotificationChannelType]**](NotificationChannelType.md) | The channels notifications on the topic are delivered through. | [optional] 
**created_at** | **str** | When the subscription was created. | [optional] 
**enabled** | **bool** | Whether notifications on the topic are delivered. | [optional] 
**id** | **str** | The identifier of the subscription. | [optional] 
**org_id** | **str** | The organization the subscription belongs to. | [optional] 
**system** | **bool** | True for a subscription AstroPulse keeps for every organization. | [optional] 
**topic** | [**NotificationTopic**](NotificationTopic.md) | The notification topic; absent for a topic AstroPulse no longer offers. | [optional] 
**updated_at** | **str** | When the subscription was last changed. | [optional] 

## Example

```python
from astropulse._generated.models.notification_subscription import NotificationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubscription from a JSON string
notification_subscription_instance = NotificationSubscription.from_json(json)
# print the JSON string representation of the object
print(NotificationSubscription.to_json())

# convert the object into a dict
notification_subscription_dict = notification_subscription_instance.to_dict()
# create an instance of NotificationSubscription from a dict
notification_subscription_from_dict = NotificationSubscription.from_dict(notification_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


