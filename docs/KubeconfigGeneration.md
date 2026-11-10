# KubeconfigGeneration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster the kubeconfig is for. | [optional] 
**error** | [**Failure**](Failure.md) | Says why generation failed, when it did. | [optional] 
**kubeconfig** | [**Kubeconfig**](Kubeconfig.md) | Present once there is one. | [optional] 
**status** | [**KubeconfigState**](KubeconfigState.md) | How far generation has got. Poll the GET endpoint until it is Provisioned. | [optional] 

## Example

```python
from astropulse._generated.models.kubeconfig_generation import KubeconfigGeneration

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigGeneration from a JSON string
kubeconfig_generation_instance = KubeconfigGeneration.from_json(json)
# print the JSON string representation of the object
print(KubeconfigGeneration.to_json())

# convert the object into a dict
kubeconfig_generation_dict = kubeconfig_generation_instance.to_dict()
# create an instance of KubeconfigGeneration from a dict
kubeconfig_generation_from_dict = KubeconfigGeneration.from_dict(kubeconfig_generation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


