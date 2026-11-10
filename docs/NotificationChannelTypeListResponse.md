# NotificationChannelTypeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NotificationChannelType]**](NotificationChannelType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.notification_channel_type_list_response import NotificationChannelTypeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelTypeListResponse from a JSON string
notification_channel_type_list_response_instance = NotificationChannelTypeListResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelTypeListResponse.to_json())

# convert the object into a dict
notification_channel_type_list_response_dict = notification_channel_type_list_response_instance.to_dict()
# create an instance of NotificationChannelTypeListResponse from a dict
notification_channel_type_list_response_from_dict = NotificationChannelTypeListResponse.from_dict(notification_channel_type_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


