# AddonResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | An amount of CPU in cores, from 10m to 16; 250m is a quarter of a core. Left out, an update keeps the current value. | [optional] 
**memory** | **str** | An amount of memory, such as 512Mi, from 64Mi (or the component&#39;s default where that is lower) to 64Gi (64 GiB). Left out, an update keeps the current value; where AstroPulse sets a memory limit and you set none, a memory request is also the limit. | [optional] 

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


