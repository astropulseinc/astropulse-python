# AddonComponentSizing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**AddonResourceRequirements**](AddonResourceRequirements.md) | The CPU and memory this component reserves and may use. Settings left out keep their current value. | [optional] 

## Example

```python
from astropulse._generated.models.addon_component_sizing import AddonComponentSizing

# TODO update the JSON string below
json = "{}"
# create an instance of AddonComponentSizing from a JSON string
addon_component_sizing_instance = AddonComponentSizing.from_json(json)
# print the JSON string representation of the object
print(AddonComponentSizing.to_json())

# convert the object into a dict
addon_component_sizing_dict = addon_component_sizing_instance.to_dict()
# create an instance of AddonComponentSizing from a dict
addon_component_sizing_from_dict = AddonComponentSizing.from_dict(addon_component_sizing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


