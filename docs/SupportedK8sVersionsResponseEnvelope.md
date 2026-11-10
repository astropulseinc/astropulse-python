# SupportedK8sVersionsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SupportedK8sVersionsResponse**](SupportedK8sVersionsResponse.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.supported_k8s_versions_response_envelope import SupportedK8sVersionsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedK8sVersionsResponseEnvelope from a JSON string
supported_k8s_versions_response_envelope_instance = SupportedK8sVersionsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupportedK8sVersionsResponseEnvelope.to_json())

# convert the object into a dict
supported_k8s_versions_response_envelope_dict = supported_k8s_versions_response_envelope_instance.to_dict()
# create an instance of SupportedK8sVersionsResponseEnvelope from a dict
supported_k8s_versions_response_envelope_from_dict = SupportedK8sVersionsResponseEnvelope.from_dict(supported_k8s_versions_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


