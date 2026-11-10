# PricingDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PricingData**](PricingData.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.pricing_data_response import PricingDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricingDataResponse from a JSON string
pricing_data_response_instance = PricingDataResponse.from_json(json)
# print the JSON string representation of the object
print(PricingDataResponse.to_json())

# convert the object into a dict
pricing_data_response_dict = pricing_data_response_instance.to_dict()
# create an instance of PricingDataResponse from a dict
pricing_data_response_from_dict = PricingDataResponse.from_dict(pricing_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


