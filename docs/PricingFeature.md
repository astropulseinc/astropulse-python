# PricingFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**developer** | [**PricingFeatureValue**](PricingFeatureValue.md) |  | [optional] 
**enterprise** | [**PricingFeatureValue**](PricingFeatureValue.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.pricing_feature import PricingFeature

# TODO update the JSON string below
json = "{}"
# create an instance of PricingFeature from a JSON string
pricing_feature_instance = PricingFeature.from_json(json)
# print the JSON string representation of the object
print(PricingFeature.to_json())

# convert the object into a dict
pricing_feature_dict = pricing_feature_instance.to_dict()
# create an instance of PricingFeature from a dict
pricing_feature_from_dict = PricingFeature.from_dict(pricing_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


