# AddonAutoScalingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Turns automatic scaling on. | [optional] 
**max_replicas** | **int** | The most copies that may run. Left out, AstroPulse&#39;s default applies. | [optional] 
**min_replicas** | **int** | The fewest copies that keep running. Left out, AstroPulse&#39;s default applies. | [optional] 
**target_cpu_percent** | **int** | The average CPU use, in percent, that scaling keeps each copy at. | [optional] 

## Example

```python
from astropulse._generated.models.addon_auto_scaling_config import AddonAutoScalingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AddonAutoScalingConfig from a JSON string
addon_auto_scaling_config_instance = AddonAutoScalingConfig.from_json(json)
# print the JSON string representation of the object
print(AddonAutoScalingConfig.to_json())

# convert the object into a dict
addon_auto_scaling_config_dict = addon_auto_scaling_config_instance.to_dict()
# create an instance of AddonAutoScalingConfig from a dict
addon_auto_scaling_config_from_dict = AddonAutoScalingConfig.from_dict(addon_auto_scaling_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


