# PricingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[PricingCategory]**](PricingCategory.md) |  | [optional] 
**plans** | [**List[PricingPlan]**](PricingPlan.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.pricing_data import PricingData

# TODO update the JSON string below
json = "{}"
# create an instance of PricingData from a JSON string
pricing_data_instance = PricingData.from_json(json)
# print the JSON string representation of the object
print(PricingData.to_json())

# convert the object into a dict
pricing_data_dict = pricing_data_instance.to_dict()
# create an instance of PricingData from a dict
pricing_data_from_dict = PricingData.from_dict(pricing_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


