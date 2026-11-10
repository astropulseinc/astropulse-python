# TierConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | [**Container**](Container.md) |  | [optional] 
**horizontal_auto_scaling** | [**HPA**](HPA.md) |  | [optional] 
**id** | **str** |  | [optional] 
**multi_zone_deployment** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**placement_preference** | [**AffinityType**](AffinityType.md) |  | [optional] 
**priority_level** | [**PriorityClassType**](PriorityClassType.md) |  | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**vertical_auto_scaling** | [**VPA**](VPA.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.tier_config import TierConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TierConfig from a JSON string
tier_config_instance = TierConfig.from_json(json)
# print the JSON string representation of the object
print(TierConfig.to_json())

# convert the object into a dict
tier_config_dict = tier_config_instance.to_dict()
# create an instance of TierConfig from a dict
tier_config_from_dict = TierConfig.from_dict(tier_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


