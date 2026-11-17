# PlanUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlanUsage**](PlanUsage.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.plan_usage_response import PlanUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanUsageResponse from a JSON string
plan_usage_response_instance = PlanUsageResponse.from_json(json)
# print the JSON string representation of the object
print(PlanUsageResponse.to_json())

# convert the object into a dict
plan_usage_response_dict = plan_usage_response_instance.to_dict()
# create an instance of PlanUsageResponse from a dict
plan_usage_response_from_dict = PlanUsageResponse.from_dict(plan_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


