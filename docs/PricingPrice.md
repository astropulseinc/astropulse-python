# PricingPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly** | **float** |  | [optional] 
**yearly** | **float** |  | [optional] 

## Example

```python
from astropulse._generated.models.pricing_price import PricingPrice

# TODO update the JSON string below
json = "{}"
# create an instance of PricingPrice from a JSON string
pricing_price_instance = PricingPrice.from_json(json)
# print the JSON string representation of the object
print(PricingPrice.to_json())

# convert the object into a dict
pricing_price_dict = pricing_price_instance.to_dict()
# create an instance of PricingPrice from a dict
pricing_price_from_dict = PricingPrice.from_dict(pricing_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


