# NotificationIntegrationConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The email recipients of an email integration. | [optional] 
**bot_token_ref** | **str** | The bot token of a Slack app installation. | [optional] 
**channel** | **str** | The Slack channel notifications are posted to. | [optional] 
**enabled** | **bool** | Whether the delivery channel is enabled. | [optional] 
**installed_by** | **List[str]** | The users who installed the Slack app. | [optional] 
**type** | [**SlackConfigType**](SlackConfigType.md) | How a Slack integration is connected; a Slack app is refused. | [optional] 
**webhook_url** | **str** | The Slack incoming webhook URL. Leave it out, or send back the masked URL, to keep the saved one. | [optional] 
**workspace_id** | **str** | The Slack workspace of an app installation. | [optional] 

## Example

```python
from astropulse._generated.models.notification_integration_config_request import NotificationIntegrationConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationIntegrationConfigRequest from a JSON string
notification_integration_config_request_instance = NotificationIntegrationConfigRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationIntegrationConfigRequest.to_json())

# convert the object into a dict
notification_integration_config_request_dict = notification_integration_config_request_instance.to_dict()
# create an instance of NotificationIntegrationConfigRequest from a dict
notification_integration_config_request_from_dict = NotificationIntegrationConfigRequest.from_dict(notification_integration_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


