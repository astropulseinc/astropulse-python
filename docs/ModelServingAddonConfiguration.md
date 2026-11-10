# ModelServingAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_access** | [**CloudAccessMode**](CloudAccessMode.md) | How model-serving reaches private model storage. Left out, it is Identity when identity is set, Secret when secretRef is set, and None otherwise; a read returns the one in use. | [optional] 
**identity** | [**AddonWorkloadIdentity**](AddonWorkloadIdentity.md) | Binds the cluster&#39;s models, and the weight cache&#39;s downloads, to a cloud workload identity so they can read private artifacts. | [optional] 
**model_cache** | [**ModelServingCacheConfiguration**](ModelServingCacheConfiguration.md) | Keeps model weights on the cluster, so a replica starting where they are held reads them instead of downloading them. Left off, every replica downloads its own weights. | [optional] 
**secret_ref** | **str** | Names a Secret in the add-on&#39;s namespace that the cluster&#39;s models read private artifacts with. Use it only where a workload identity cannot be used; it cannot be combined with identity. | [optional] 

## Example

```python
from astropulse._generated.models.model_serving_addon_configuration import ModelServingAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ModelServingAddonConfiguration from a JSON string
model_serving_addon_configuration_instance = ModelServingAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(ModelServingAddonConfiguration.to_json())

# convert the object into a dict
model_serving_addon_configuration_dict = model_serving_addon_configuration_instance.to_dict()
# create an instance of ModelServingAddonConfiguration from a dict
model_serving_addon_configuration_from_dict = ModelServingAddonConfiguration.from_dict(model_serving_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


