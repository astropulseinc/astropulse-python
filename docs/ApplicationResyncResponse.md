# ApplicationResyncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationResync**](ApplicationResync.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_resync_response import ApplicationResyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResyncResponse from a JSON string
application_resync_response_instance = ApplicationResyncResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationResyncResponse.to_json())

# convert the object into a dict
application_resync_response_dict = application_resync_response_instance.to_dict()
# create an instance of ApplicationResyncResponse from a dict
application_resync_response_from_dict = ApplicationResyncResponse.from_dict(application_resync_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


