# ModelServingAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_access** | [**CloudAccessMode**](CloudAccessMode.md) | How models sign in to private model storage. Left out, it is &#x60;Identity&#x60; when &#x60;identity&#x60; is set, &#x60;Secret&#x60; when &#x60;secretRef&#x60; is set, and &#x60;None&#x60; otherwise. | [optional] 
**identity** | [**AddonWorkloadIdentity**](AddonWorkloadIdentity.md) | The cloud identity models and the weight cache run as to read private model files. | [optional] 
**model_cache** | [**ModelServingCacheConfiguration**](ModelServingCacheConfiguration.md) | Keeps model weights on the cluster, so a replica starting where they are held reads them instead of downloading them. Left out, every replica downloads its own weights. | [optional] 
**secret_ref** | **str** | The name of a Secret in the add-on&#39;s namespace that models read private model files with. Use it only where a cloud identity can&#39;t be used; it can&#39;t be combined with &#x60;identity&#x60;. | [optional] 

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


