# UpgradePlanNodePoolState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_type** | [**InstanceType**](InstanceType.md) | How the node pool&#39;s nodes are bought. | [optional] 
**machine_types** | **List[str]** | Lists the instance types. | [optional] 
**max_nodes** | **int** | The maximum node count. | [optional] 
**min_nodes** | **int** | The minimum node count. | [optional] 

## Example

```python
from astropulse._generated.models.upgrade_plan_node_pool_state import UpgradePlanNodePoolState

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradePlanNodePoolState from a JSON string
upgrade_plan_node_pool_state_instance = UpgradePlanNodePoolState.from_json(json)
# print the JSON string representation of the object
print(UpgradePlanNodePoolState.to_json())

# convert the object into a dict
upgrade_plan_node_pool_state_dict = upgrade_plan_node_pool_state_instance.to_dict()
# create an instance of UpgradePlanNodePoolState from a dict
upgrade_plan_node_pool_state_from_dict = UpgradePlanNodePoolState.from_dict(upgrade_plan_node_pool_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


