# ApplicationResync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The name/ID of the application that was resynced | [optional] 
**force** | **bool** | Indicates whether this was a forced resync | [optional] 
**message** | **str** | A human-readable message about the operation | [optional] 
**status** | [**ApplicationResyncStatus**](ApplicationResyncStatus.md) | What the request did; absent when it could not be told. | [optional] 

## Example

```python
from astropulse._generated.models.application_resync import ApplicationResync

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResync from a JSON string
application_resync_instance = ApplicationResync.from_json(json)
# print the JSON string representation of the object
print(ApplicationResync.to_json())

# convert the object into a dict
application_resync_dict = application_resync_instance.to_dict()
# create an instance of ApplicationResync from a dict
application_resync_from_dict = ApplicationResync.from_dict(application_resync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


