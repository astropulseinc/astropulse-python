# NotificationIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**NotificationChannelType**](NotificationChannelType.md) | The channel notifications are delivered through. | [optional] 
**config** | [**NotificationIntegrationConfig**](NotificationIntegrationConfig.md) |  | [optional] 
**created_at** | **str** | When the integration was first configured | [optional] 
**enabled** | **bool** | Reports whether notifications are delivered through this channel | [optional] 
**id** | **str** | The identifier of the integration | [optional] 
**org_id** | **str** | The organization the integration belongs to | [optional] 
**updated_at** | **str** | When the integration was last changed | [optional] 

## Example

```python
from astropulse._generated.models.notification_integration import NotificationIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationIntegration from a JSON string
notification_integration_instance = NotificationIntegration.from_json(json)
# print the JSON string representation of the object
print(NotificationIntegration.to_json())

# convert the object into a dict
notification_integration_dict = notification_integration_instance.to_dict()
# create an instance of NotificationIntegration from a dict
notification_integration_from_dict = NotificationIntegration.from_dict(notification_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


