# ApplicationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Application]**](Application.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_list_response import ApplicationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationListResponse from a JSON string
application_list_response_instance = ApplicationListResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationListResponse.to_json())

# convert the object into a dict
application_list_response_dict = application_list_response_instance.to_dict()
# create an instance of ApplicationListResponse from a dict
application_list_response_from_dict = ApplicationListResponse.from_dict(application_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


