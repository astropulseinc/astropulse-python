# CloudConnectAttemptError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Says what failed and what happens next, ready to show as is. | [optional] 
**reason** | [**CloudConnectFailureReason**](CloudConnectFailureReason.md) | What kind of failure it was. | [optional] 
**retrying** | **bool** | True while AstroPulse keeps checking, and false once it has stopped. | [optional] 
**since** | **str** | When AstroPulse started checking the account. | [optional] 

## Example

```python
from astropulse._generated.models.cloud_connect_attempt_error import CloudConnectAttemptError

# TODO update the JSON string below
json = "{}"
# create an instance of CloudConnectAttemptError from a JSON string
cloud_connect_attempt_error_instance = CloudConnectAttemptError.from_json(json)
# print the JSON string representation of the object
print(CloudConnectAttemptError.to_json())

# convert the object into a dict
cloud_connect_attempt_error_dict = cloud_connect_attempt_error_instance.to_dict()
# create an instance of CloudConnectAttemptError from a dict
cloud_connect_attempt_error_from_dict = CloudConnectAttemptError.from_dict(cloud_connect_attempt_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


