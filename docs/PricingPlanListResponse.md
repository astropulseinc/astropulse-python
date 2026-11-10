# PricingPlanListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PricingPlan]**](PricingPlan.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.pricing_plan_list_response import PricingPlanListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricingPlanListResponse from a JSON string
pricing_plan_list_response_instance = PricingPlanListResponse.from_json(json)
# print the JSON string representation of the object
print(PricingPlanListResponse.to_json())

# convert the object into a dict
pricing_plan_list_response_dict = pricing_plan_list_response_instance.to_dict()
# create an instance of PricingPlanListResponse from a dict
pricing_plan_list_response_from_dict = PricingPlanListResponse.from_dict(pricing_plan_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


