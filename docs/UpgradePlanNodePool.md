# UpgradePlanNodePool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_type** | [**NodeGroupChangeType**](NodeGroupChangeType.md) | Describes what is changing for this node pool. | [optional] 
**current** | [**UpgradePlanNodePoolState**](UpgradePlanNodePoolState.md) | The node pool as it is before the update; absent for a node pool the update creates. | [optional] 
**instance_type** | [**InstanceType**](InstanceType.md) | How the node pool&#39;s nodes are bought once the update is applied. | [optional] 
**machine_types** | **List[str]** | Lists the instance types in this node pool once the update is applied. | [optional] 
**max_nodes** | **int** | The maximum node count once the update is applied. | [optional] 
**min_nodes** | **int** | The minimum node count once the update is applied. | [optional] 
**name** | **str** | The node pool name | [optional] 
**strategy** | [**NodeGroupUpdateStrategy**](NodeGroupUpdateStrategy.md) | Describes how this specific node pool will be updated. | [optional] 

## Example

```python
from astropulse._generated.models.upgrade_plan_node_pool import UpgradePlanNodePool

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradePlanNodePool from a JSON string
upgrade_plan_node_pool_instance = UpgradePlanNodePool.from_json(json)
# print the JSON string representation of the object
print(UpgradePlanNodePool.to_json())

# convert the object into a dict
upgrade_plan_node_pool_dict = upgrade_plan_node_pool_instance.to_dict()
# create an instance of UpgradePlanNodePool from a dict
upgrade_plan_node_pool_from_dict = UpgradePlanNodePool.from_dict(upgrade_plan_node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


