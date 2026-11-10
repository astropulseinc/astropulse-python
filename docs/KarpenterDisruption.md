# KarpenterDisruption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgets** | [**List[KarpenterDisruptionBudget]**](KarpenterDisruptionBudget.md) | Limits on how many nodes change at once; when several apply, the smallest wins. Omit them for one budget of 10%. | [optional] 
**consolidate_after** | **str** | How long a node stays empty or underused before it is removed: 30s (5m on the GPU pool) to 720h, or Never. Shorter saves idle cost; longer keeps the node for the next workload, which then avoids waiting for a new one. | [optional] 
**consolidation_policy** | [**KarpenterConsolidationPolicy**](KarpenterConsolidationPolicy.md) | Either WhenEmpty (remove only nodes with nothing left running) or WhenEmptyOrUnderutilized (also move workloads onto fewer, cheaper nodes to save cost; pods restart when they are moved). | [optional] 

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


