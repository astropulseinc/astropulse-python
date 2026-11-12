# AddonResourceRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**AddonResources**](AddonResources.md) | The most CPU and memory the component may use, at least &#x60;requests&#x60;. Where AstroPulse sets a limit and you set none, the memory request is also the memory limit and the CPU limit is at least the CPU request; set &#x60;limits&#x60; to make them differ. | [optional] 
**requests** | [**AddonResources**](AddonResources.md) | The CPU and memory set aside for the component. Left out, an update keeps the current values and a new add-on gets AstroPulse&#39;s sizing. | [optional] 

## Example

```python
from astropulse._generated.models.addon_resource_requirements import AddonResourceRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResourceRequirements from a JSON string
addon_resource_requirements_instance = AddonResourceRequirements.from_json(json)
# print the JSON string representation of the object
print(AddonResourceRequirements.to_json())

# convert the object into a dict
addon_resource_requirements_dict = addon_resource_requirements_instance.to_dict()
# create an instance of AddonResourceRequirements from a dict
addon_resource_requirements_from_dict = AddonResourceRequirements.from_dict(addon_resource_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


