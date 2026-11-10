# DeleteAPIKeyResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteAPIKeyResponse**](DeleteAPIKeyResponse.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.delete_api_key_response_envelope import DeleteAPIKeyResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAPIKeyResponseEnvelope from a JSON string
delete_api_key_response_envelope_instance = DeleteAPIKeyResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(DeleteAPIKeyResponseEnvelope.to_json())

# convert the object into a dict
delete_api_key_response_envelope_dict = delete_api_key_response_envelope_instance.to_dict()
# create an instance of DeleteAPIKeyResponseEnvelope from a dict
delete_api_key_response_envelope_from_dict = DeleteAPIKeyResponseEnvelope.from_dict(delete_api_key_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


