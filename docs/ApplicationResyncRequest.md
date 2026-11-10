# ApplicationResyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Sync even if no changes detected or previous operation is stuck Useful when previous deployments are stuck in terminating state | [optional] 

## Example

```python
from astropulse._generated.models.application_resync_request import ApplicationResyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResyncRequest from a JSON string
application_resync_request_instance = ApplicationResyncRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationResyncRequest.to_json())

# convert the object into a dict
application_resync_request_dict = application_resync_request_instance.to_dict()
# create an instance of ApplicationResyncRequest from a dict
application_resync_request_from_dict = ApplicationResyncRequest.from_dict(application_resync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


