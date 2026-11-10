# GCPConnectStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GCPConnectStatus**](GCPConnectStatus.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.gcp_connect_status_response import GCPConnectStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GCPConnectStatusResponse from a JSON string
gcp_connect_status_response_instance = GCPConnectStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GCPConnectStatusResponse.to_json())

# convert the object into a dict
gcp_connect_status_response_dict = gcp_connect_status_response_instance.to_dict()
# create an instance of GCPConnectStatusResponse from a dict
gcp_connect_status_response_from_dict = GCPConnectStatusResponse.from_dict(gcp_connect_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


