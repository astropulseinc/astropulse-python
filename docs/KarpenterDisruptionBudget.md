# KarpenterDisruptionBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | How long the budget lasts after each start, such as 8h or 1h30m; set it with &#x60;schedule&#x60;. | [optional] 
**nodes** | **str** | The most nodes that may change at once, as a count such as 2 or a share of the pool such as 10%; 0 stops removals. | [optional] 
**reasons** | **List[str]** | The causes of removal the budget applies to. Left out, it applies to all of them. | [optional] 
**schedule** | **str** | When the budget starts, as a five-field cron expression in UTC or a shortcut such as @daily; set it with &#x60;duration&#x60;. | [optional] 

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


