# KarpenterDisruption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgets** | [**List[KarpenterDisruptionBudget]**](KarpenterDisruptionBudget.md) | Limits on how many nodes change at once; when several apply, the smallest wins. Left out, it is one budget of 10%. | [optional] 
**consolidate_after** | **str** | How long a node stays empty or underused before it is removed, from 30s (5m for GPU nodes) to 720h, or &#x60;Never&#x60;. Shorter saves idle cost; longer keeps the node ready for the next workload. | [optional] 
**consolidation_policy** | [**KarpenterConsolidationPolicy**](KarpenterConsolidationPolicy.md) | Which nodes may be removed: only empty ones, or also underused ones, whose pods restart on fewer, cheaper nodes. | [optional] 

## Example

```python
from astropulse._generated.models.karpenter_disruption import KarpenterDisruption

# TODO update the JSON string below
json = "{}"
# create an instance of KarpenterDisruption from a JSON string
karpenter_disruption_instance = KarpenterDisruption.from_json(json)
# print the JSON string representation of the object
print(KarpenterDisruption.to_json())

# convert the object into a dict
karpenter_disruption_dict = karpenter_disruption_instance.to_dict()
# create an instance of KarpenterDisruption from a dict
karpenter_disruption_from_dict = KarpenterDisruption.from_dict(karpenter_disruption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


