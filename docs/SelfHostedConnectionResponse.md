# SelfHostedConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SelfHostedConnection**](SelfHostedConnection.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_connection_response import SelfHostedConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedConnectionResponse from a JSON string
self_hosted_connection_response_instance = SelfHostedConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(SelfHostedConnectionResponse.to_json())

# convert the object into a dict
self_hosted_connection_response_dict = self_hosted_connection_response_instance.to_dict()
# create an instance of SelfHostedConnectionResponse from a dict
self_hosted_connection_response_from_dict = SelfHostedConnectionResponse.from_dict(self_hosted_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


