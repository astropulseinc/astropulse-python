# NotificationIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NotificationIntegration**](NotificationIntegration.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.notification_integration_response import NotificationIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationIntegrationResponse from a JSON string
notification_integration_response_instance = NotificationIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationIntegrationResponse.to_json())

# convert the object into a dict
notification_integration_response_dict = notification_integration_response_instance.to_dict()
# create an instance of NotificationIntegrationResponse from a dict
notification_integration_response_from_dict = NotificationIntegrationResponse.from_dict(notification_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


