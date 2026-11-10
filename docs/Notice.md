# Notice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**NoticeCode**](NoticeCode.md) | Identifies the notice and is unique across the API. | [optional] 
**hostname** | **str** | The hostname the application is served at, on a &#x60;HostnameTaken&#x60; notice. | [optional] 
**message** | **str** | Says in one or two sentences what happened and why. | [optional] 
**next_step** | [**NextStep**](NextStep.md) | The one thing to do, when there is one. | [optional] 
**preferred** | **str** | The hostname that was taken, on a &#x60;HostnameTaken&#x60; notice. | [optional] 
**severity** | [**NoticeSeverity**](NoticeSeverity.md) | How much the notice matters. | [optional] 
**title** | **str** | A short headline of at most 60 characters. | [optional] 

## Example

```python
from astropulse._generated.models.notice import Notice

# TODO update the JSON string below
json = "{}"
# create an instance of Notice from a JSON string
notice_instance = Notice.from_json(json)
# print the JSON string representation of the object
print(Notice.to_json())

# convert the object into a dict
notice_dict = notice_instance.to_dict()
# create an instance of Notice from a dict
notice_from_dict = Notice.from_dict(notice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


