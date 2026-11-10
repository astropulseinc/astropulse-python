# NotificationIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**NotificationChannelType**](NotificationChannelType.md) | The channel notifications are delivered through. | [optional] 
**config** | [**NotificationIntegrationConfigRequest**](NotificationIntegrationConfigRequest.md) | The channel&#39;s settings. | [optional] 
**enabled** | **bool** | Whether notifications are delivered through this channel. | [optional] 

## Example

```python
from astropulse._generated.models.notification_integration_request import NotificationIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationIntegrationRequest from a JSON string
notification_integration_request_instance = NotificationIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationIntegrationRequest.to_json())

# convert the object into a dict
notification_integration_request_dict = notification_integration_request_instance.to_dict()
# create an instance of NotificationIntegrationRequest from a dict
notification_integration_request_from_dict = NotificationIntegrationRequest.from_dict(notification_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


