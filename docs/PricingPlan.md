# PricingPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**cta** | [**PricingCta**](PricingCta.md) |  | [optional] 
**description** | **str** |  | [optional] 
**highlight** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**popular** | **bool** |  | [optional] 
**price** | [**PricingPrice**](PricingPrice.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.pricing_plan import PricingPlan

# TODO update the JSON string below
json = "{}"
# create an instance of PricingPlan from a JSON string
pricing_plan_instance = PricingPlan.from_json(json)
# print the JSON string representation of the object
print(PricingPlan.to_json())

# convert the object into a dict
pricing_plan_dict = pricing_plan_instance.to_dict()
# create an instance of PricingPlan from a dict
pricing_plan_from_dict = PricingPlan.from_dict(pricing_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


