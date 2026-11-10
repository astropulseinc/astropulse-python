# EndpointStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EndpointStatus**](EndpointStatus.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.endpoint_status_response import EndpointStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStatusResponse from a JSON string
endpoint_status_response_instance = EndpointStatusResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointStatusResponse.to_json())

# convert the object into a dict
endpoint_status_response_dict = endpoint_status_response_instance.to_dict()
# create an instance of EndpointStatusResponse from a dict
endpoint_status_response_from_dict = EndpointStatusResponse.from_dict(endpoint_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


