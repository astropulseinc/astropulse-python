# PlanLimitUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The pricing category the resource belongs to. | [optional] 
**limit** | **int** | How many the plan allows. | [optional] 
**required_plan** | **str** | The first plan above this one that allows more; absent when none does. | [optional] 
**required_plan_name** | **str** | The required plan&#39;s name, such as Enterprise. Its limits are negotiated, so no number is given. | [optional] 
**resource** | [**PlanResource**](PlanResource.md) | The resource the limit counts. | [optional] 
**state** | [**PlanLimitState**](PlanLimitState.md) | How the usage stands against the limit. | [optional] 
**used** | **int** | How many the organization uses now. | [optional] 

## Example

```python
from astropulse._generated.models.plan_limit_usage import PlanLimitUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PlanLimitUsage from a JSON string
plan_limit_usage_instance = PlanLimitUsage.from_json(json)
# print the JSON string representation of the object
print(PlanLimitUsage.to_json())

# convert the object into a dict
plan_limit_usage_dict = plan_limit_usage_instance.to_dict()
# create an instance of PlanLimitUsage from a dict
plan_limit_usage_from_dict = PlanLimitUsage.from_dict(plan_limit_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


