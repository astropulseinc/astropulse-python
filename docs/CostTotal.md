# CostTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount of the priced usage, a decimal in &#x60;currency&#x60;; an entry whose &#x60;pricingSource&#x60; is &#x60;Unpriced&#x60; marks the usage left out. | [optional] 
**currency** | **str** |  | [optional] 
**pricing_source** | [**CostPricingSource**](CostPricingSource.md) | Where the prices came from. | [optional] 
**unpriced_reasons** | [**List[Notice]**](Notice.md) | Why part of the usage has no price, on the &#x60;Unpriced&#x60; entry, each with what to do about it. | [optional] 

## Example

```python
from astropulse._generated.models.cost_total import CostTotal

# TODO update the JSON string below
json = "{}"
# create an instance of CostTotal from a JSON string
cost_total_instance = CostTotal.from_json(json)
# print the JSON string representation of the object
print(CostTotal.to_json())

# convert the object into a dict
cost_total_dict = cost_total_instance.to_dict()
# create an instance of CostTotal from a dict
cost_total_from_dict = CostTotal.from_dict(cost_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


