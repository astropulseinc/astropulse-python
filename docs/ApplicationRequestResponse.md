# ApplicationRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationRequest**](ApplicationRequest.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_request_response import ApplicationRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRequestResponse from a JSON string
application_request_response_instance = ApplicationRequestResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationRequestResponse.to_json())

# convert the object into a dict
application_request_response_dict = application_request_response_instance.to_dict()
# create an instance of ApplicationRequestResponse from a dict
application_request_response_from_dict = ApplicationRequestResponse.from_dict(application_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


