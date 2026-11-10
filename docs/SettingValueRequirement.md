# SettingValueRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The capacity the cloud account must already hold for the value, in one sentence. | [optional] 
**value** | **str** | The value, as written in the request. | [optional] 

## Example

```python
from astropulse._generated.models.setting_value_requirement import SettingValueRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of SettingValueRequirement from a JSON string
setting_value_requirement_instance = SettingValueRequirement.from_json(json)
# print the JSON string representation of the object
print(SettingValueRequirement.to_json())

# convert the object into a dict
setting_value_requirement_dict = setting_value_requirement_instance.to_dict()
# create an instance of SettingValueRequirement from a dict
setting_value_requirement_from_dict = SettingValueRequirement.from_dict(setting_value_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


