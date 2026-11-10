# PricingCta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**variant** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.pricing_cta import PricingCta

# TODO update the JSON string below
json = "{}"
# create an instance of PricingCta from a JSON string
pricing_cta_instance = PricingCta.from_json(json)
# print the JSON string representation of the object
print(PricingCta.to_json())

# convert the object into a dict
pricing_cta_dict = pricing_cta_instance.to_dict()
# create an instance of PricingCta from a dict
pricing_cta_from_dict = PricingCta.from_dict(pricing_cta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


