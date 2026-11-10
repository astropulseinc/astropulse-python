# NotificationIntegrationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | Lists the email recipients of an email integration | [optional] 
**bot_token_ref** | **str** | Names the bot token of a Slack app installation | [optional] 
**channel** | **str** | The Slack channel notifications are posted to | [optional] 
**enabled** | **bool** | Reports whether the delivery channel is enabled | [optional] 
**installed_by** | **List[str]** | Lists the users who installed the Slack app | [optional] 
**type** | [**SlackConfigType**](SlackConfigType.md) | How a Slack integration is connected. | [optional] 
**webhook_configured** | **bool** | Reports whether a Slack webhook URL is saved for this channel. The saved URL is never returned in full. | [optional] 
**webhook_url** | **str** | The saved Slack webhook URL with its secret part replaced by asterisks. To keep the saved URL, leave this field out or send it back unchanged; to change it, send a complete new URL. | [optional] 
**workspace_id** | **str** | The Slack workspace of an app installation | [optional] 

## Example

```python
from astropulse._generated.models.notification_integration_config import NotificationIntegrationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationIntegrationConfig from a JSON string
notification_integration_config_instance = NotificationIntegrationConfig.from_json(json)
# print the JSON string representation of the object
print(NotificationIntegrationConfig.to_json())

# convert the object into a dict
notification_integration_config_dict = notification_integration_config_instance.to_dict()
# create an instance of NotificationIntegrationConfig from a dict
notification_integration_config_from_dict = NotificationIntegrationConfig.from_dict(notification_integration_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


