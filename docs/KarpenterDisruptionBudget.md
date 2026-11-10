# KarpenterDisruptionBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | How long the budget lasts after each schedule start, in hours and minutes such as 8h or 1h30m; set with schedule. | [optional] 
**nodes** | **str** | The most nodes that may change at once, as a count (2) or a percentage of the pool (10%); 0 stops removals, so idle nodes keep being billed. | [optional] 
**reasons** | **List[str]** | Limits the budget to these causes: Empty, Underutilized, Drifted (out of date with its settings) or Unhealthy; omit for all. | [optional] 
**schedule** | **str** | When the budget starts, as a five-field cron expression in UTC or @hourly, @daily, @weekly, @monthly or @yearly; set with duration. | [optional] 

## Example

```python
from astropulse._generated.models.karpenter_disruption_budget import KarpenterDisruptionBudget

# TODO update the JSON string below
json = "{}"
# create an instance of KarpenterDisruptionBudget from a JSON string
karpenter_disruption_budget_instance = KarpenterDisruptionBudget.from_json(json)
# print the JSON string representation of the object
print(KarpenterDisruptionBudget.to_json())

# convert the object into a dict
karpenter_disruption_budget_dict = karpenter_disruption_budget_instance.to_dict()
# create an instance of KarpenterDisruptionBudget from a dict
karpenter_disruption_budget_from_dict = KarpenterDisruptionBudget.from_dict(karpenter_disruption_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


