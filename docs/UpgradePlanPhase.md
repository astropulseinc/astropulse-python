# UpgradePlanPhase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Explains what happens during this phase | [optional] 
**details** | **List[str]** | Provides additional context about this phase | [optional] 
**estimated_duration** | **str** | The expected time for this phase (e.g. \&quot;5m\&quot;, \&quot;15m\&quot;) | [optional] 
**name** | **str** | The phase identifier (e.g. \&quot;Control Plane Upgrade\&quot;, \&quot;Node Pool Rolling Update\&quot;) | [optional] 
**node_pools** | [**List[UpgradePlanNodePool]**](UpgradePlanNodePool.md) | Lists the node pools affected by this phase | [optional] 
**strategy** | [**NodeGroupUpdateStrategy**](NodeGroupUpdateStrategy.md) | Describes how this phase will be executed. Automatically selected based on what is changing and the provider&#39;s capabilities. | [optional] 

## Example

```python
from astropulse._generated.models.upgrade_plan_phase import UpgradePlanPhase

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradePlanPhase from a JSON string
upgrade_plan_phase_instance = UpgradePlanPhase.from_json(json)
# print the JSON string representation of the object
print(UpgradePlanPhase.to_json())

# convert the object into a dict
upgrade_plan_phase_dict = upgrade_plan_phase_instance.to_dict()
# create an instance of UpgradePlanPhase from a dict
upgrade_plan_phase_from_dict = UpgradePlanPhase.from_dict(upgrade_plan_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


