# CloudConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CloudConnection**](CloudConnection.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cloud_connection_response import CloudConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudConnectionResponse from a JSON string
cloud_connection_response_instance = CloudConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(CloudConnectionResponse.to_json())

# convert the object into a dict
cloud_connection_response_dict = cloud_connection_response_instance.to_dict()
# create an instance of CloudConnectionResponse from a dict
cloud_connection_response_from_dict = CloudConnectionResponse.from_dict(cloud_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


