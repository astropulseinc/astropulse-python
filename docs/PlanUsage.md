# PlanUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**List[PlanLimitUsage]**](PlanLimitUsage.md) | One entry per resource the plan limits by number; a resource with no limit is left out. | [optional] 
**plan** | **str** | The plan&#39;s id, such as developer. | [optional] 
**plan_name** | **str** | The plan&#39;s name, such as Developer. | [optional] 

## Example

```python
from astropulse._generated.models.plan_usage import PlanUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PlanUsage from a JSON string
plan_usage_instance = PlanUsage.from_json(json)
# print the JSON string representation of the object
print(PlanUsage.to_json())

# convert the object into a dict
plan_usage_dict = plan_usage_instance.to_dict()
# create an instance of PlanUsage from a dict
plan_usage_from_dict = PlanUsage.from_dict(plan_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


