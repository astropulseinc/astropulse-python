# EndpointChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation** | **int** |  | [optional] 

## Example

```python
from astropulse._generated.models.endpoint_change_request import EndpointChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointChangeRequest from a JSON string
endpoint_change_request_instance = EndpointChangeRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointChangeRequest.to_json())

# convert the object into a dict
endpoint_change_request_dict = endpoint_change_request_instance.to_dict()
# create an instance of EndpointChangeRequest from a dict
endpoint_change_request_from_dict = EndpointChangeRequest.from_dict(endpoint_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


