# NotificationTopicListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NotificationTopic]**](NotificationTopic.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.notification_topic_list_response import NotificationTopicListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTopicListResponse from a JSON string
notification_topic_list_response_instance = NotificationTopicListResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationTopicListResponse.to_json())

# convert the object into a dict
notification_topic_list_response_dict = notification_topic_list_response_instance.to_dict()
# create an instance of NotificationTopicListResponse from a dict
notification_topic_list_response_from_dict = NotificationTopicListResponse.from_dict(notification_topic_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


