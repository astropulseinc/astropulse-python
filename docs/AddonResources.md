# AddonResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | The CPU reserved for the component, in cores: 250m is a quarter of a core, from 10m (0.01 cores) to 16 cores. Left out, an update keeps the current value and a new add-on gets AstroPulse&#39;s sizing. | [optional] 
**memory** | **str** | The memory reserved for the component, such as 512Mi (512 MiB), from 64Mi (64 MiB) to 64Gi (64 GiB). Left out, an update keeps the current value and a new add-on gets AstroPulse&#39;s sizing. | [optional] 

## Example

```python
from astropulse._generated.models.addon_resources import AddonResources

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResources from a JSON string
addon_resources_instance = AddonResources.from_json(json)
# print the JSON string representation of the object
print(AddonResources.to_json())

# convert the object into a dict
addon_resources_dict = addon_resources_instance.to_dict()
# create an instance of AddonResources from a dict
addon_resources_from_dict = AddonResources.from_dict(addon_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


