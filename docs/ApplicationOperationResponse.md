# ApplicationOperationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationOperation**](ApplicationOperation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_operation_response import ApplicationOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationOperationResponse from a JSON string
application_operation_response_instance = ApplicationOperationResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationOperationResponse.to_json())

# convert the object into a dict
application_operation_response_dict = application_operation_response_instance.to_dict()
# create an instance of ApplicationOperationResponse from a dict
application_operation_response_from_dict = ApplicationOperationResponse.from_dict(application_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


