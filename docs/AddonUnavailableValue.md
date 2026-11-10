# AddonUnavailableValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Why the cluster does not offer it, and what would. | [optional] 
**value** | **str** | The value, as written in the configuration. | [optional] 

## Example

```python
from astropulse._generated.models.addon_unavailable_value import AddonUnavailableValue

# TODO update the JSON string below
json = "{}"
# create an instance of AddonUnavailableValue from a JSON string
addon_unavailable_value_instance = AddonUnavailableValue.from_json(json)
# print the JSON string representation of the object
print(AddonUnavailableValue.to_json())

# convert the object into a dict
addon_unavailable_value_dict = addon_unavailable_value_instance.to_dict()
# create an instance of AddonUnavailableValue from a dict
addon_unavailable_value_from_dict = AddonUnavailableValue.from_dict(addon_unavailable_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


