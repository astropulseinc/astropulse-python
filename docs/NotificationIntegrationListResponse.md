# NotificationIntegrationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NotificationIntegration]**](NotificationIntegration.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.notification_integration_list_response import NotificationIntegrationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationIntegrationListResponse from a JSON string
notification_integration_list_response_instance = NotificationIntegrationListResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationIntegrationListResponse.to_json())

# convert the object into a dict
notification_integration_list_response_dict = notification_integration_list_response_instance.to_dict()
# create an instance of NotificationIntegrationListResponse from a dict
notification_integration_list_response_from_dict = NotificationIntegrationListResponse.from_dict(notification_integration_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


