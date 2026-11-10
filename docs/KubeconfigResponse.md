# KubeconfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytes** | The kubeconfig file, base64-encoded. | [optional] 
**id** | **str** | Identifies the response, when one is set. | [optional] 
**message** | **str** | Describes the result, when there is more to say. | [optional] 
**status** | [**KubeconfigState**](KubeconfigState.md) | The state of the kubeconfig, such as Provisioned. | [optional] 

## Example

```python
from astropulse._generated.models.kubeconfig_response import KubeconfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigResponse from a JSON string
kubeconfig_response_instance = KubeconfigResponse.from_json(json)
# print the JSON string representation of the object
print(KubeconfigResponse.to_json())

# convert the object into a dict
kubeconfig_response_dict = kubeconfig_response_instance.to_dict()
# create an instance of KubeconfigResponse from a dict
kubeconfig_response_from_dict = KubeconfigResponse.from_dict(kubeconfig_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


