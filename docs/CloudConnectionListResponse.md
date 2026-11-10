# CloudConnectionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CloudConnection]**](CloudConnection.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cloud_connection_list_response import CloudConnectionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudConnectionListResponse from a JSON string
cloud_connection_list_response_instance = CloudConnectionListResponse.from_json(json)
# print the JSON string representation of the object
print(CloudConnectionListResponse.to_json())

# convert the object into a dict
cloud_connection_list_response_dict = cloud_connection_list_response_instance.to_dict()
# create an instance of CloudConnectionListResponse from a dict
cloud_connection_list_response_from_dict = CloudConnectionListResponse.from_dict(cloud_connection_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


