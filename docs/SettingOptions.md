# SettingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | The value used when the field is omitted; absent when there is none. | [optional] 
**default_reason** | **str** | Why &#x60;default&#x60; is the value used, in one sentence; absent when there is no default. | [optional] 
**description** | **str** | What the setting controls, in one sentence. | [optional] 
**enum** | **List[str]** | The accepted values, in the order to offer them; absent for a text setting, which has a &#x60;format&#x60;. | [optional] 
**var_field** | **str** | The request field the values are for, such as &#x60;releaseChannel&#x60;. | [optional] 
**format** | [**SettingFormat**](SettingFormat.md) | The form a text setting&#39;s value takes; for a list, the form of each entry. Absent for a setting with &#x60;enum&#x60;. | [optional] 
**label** | **str** | The setting&#39;s name for people, such as Release channel. | [optional] 
**max_items** | **int** | The most entries a list setting accepts; absent when the setting is not a list or has no limit. | [optional] 
**requirements** | [**List[SettingValueRequirement]**](SettingValueRequirement.md) | Values in &#x60;enum&#x60; that run only on capacity the cloud account already holds, which no request field can supply, each with what that capacity must be. Absent when no value needs held capacity. | [optional] 

## Example

```python
from astropulse._generated.models.setting_options import SettingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SettingOptions from a JSON string
setting_options_instance = SettingOptions.from_json(json)
# print the JSON string representation of the object
print(SettingOptions.to_json())

# convert the object into a dict
setting_options_dict = setting_options_instance.to_dict()
# create an instance of SettingOptions from a dict
setting_options_from_dict = SettingOptions.from_dict(setting_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


