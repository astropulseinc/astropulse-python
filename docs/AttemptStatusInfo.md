# AttemptStatusInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **str** | The timestamp when the attempt completed (RFC 3339 format) | [optional] 
**reason** | **str** | Provides details about the current status or failure cause | [optional] 
**started_at** | **str** | The timestamp when the attempt started (RFC 3339 format) | [optional] 
**status** | [**AttemptStatus**](AttemptStatus.md) | The outcome of the attempt. | [optional] 
**suggested_action** | **str** | A recommended next step when the attempt fails | [optional] 

## Example

```python
from astropulse._generated.models.attempt_status_info import AttemptStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AttemptStatusInfo from a JSON string
attempt_status_info_instance = AttemptStatusInfo.from_json(json)
# print the JSON string representation of the object
print(AttemptStatusInfo.to_json())

# convert the object into a dict
attempt_status_info_dict = attempt_status_info_instance.to_dict()
# create an instance of AttemptStatusInfo from a dict
attempt_status_info_from_dict = AttemptStatusInfo.from_dict(attempt_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


