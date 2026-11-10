# KubeconfigGenerationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**KubeconfigGeneration**](KubeconfigGeneration.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.kubeconfig_generation_response import KubeconfigGenerationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigGenerationResponse from a JSON string
kubeconfig_generation_response_instance = KubeconfigGenerationResponse.from_json(json)
# print the JSON string representation of the object
print(KubeconfigGenerationResponse.to_json())

# convert the object into a dict
kubeconfig_generation_response_dict = kubeconfig_generation_response_instance.to_dict()
# create an instance of KubeconfigGenerationResponse from a dict
kubeconfig_generation_response_from_dict = KubeconfigGenerationResponse.from_dict(kubeconfig_generation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


