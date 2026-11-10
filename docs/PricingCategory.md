# PricingCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[PricingFeature]**](PricingFeature.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.pricing_category import PricingCategory

# TODO update the JSON string below
json = "{}"
# create an instance of PricingCategory from a JSON string
pricing_category_instance = PricingCategory.from_json(json)
# print the JSON string representation of the object
print(PricingCategory.to_json())

# convert the object into a dict
pricing_category_dict = pricing_category_instance.to_dict()
# create an instance of PricingCategory from a dict
pricing_category_from_dict = PricingCategory.from_dict(pricing_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


