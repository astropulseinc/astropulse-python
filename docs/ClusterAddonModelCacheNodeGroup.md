# ClusterAddonModelCacheNodeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | **str** | The hardware its nodes carry (\&quot;nvidia a100\&quot;). | [optional] 
**name** | **str** | The node group&#39;s name, which the LocalModelNodeGroup takes. | [optional] 
**size** | **str** | The disk the cache reserves on each node of the group. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_model_cache_node_group import ClusterAddonModelCacheNodeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonModelCacheNodeGroup from a JSON string
cluster_addon_model_cache_node_group_instance = ClusterAddonModelCacheNodeGroup.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonModelCacheNodeGroup.to_json())

# convert the object into a dict
cluster_addon_model_cache_node_group_dict = cluster_addon_model_cache_node_group_instance.to_dict()
# create an instance of ClusterAddonModelCacheNodeGroup from a dict
cluster_addon_model_cache_node_group_from_dict = ClusterAddonModelCacheNodeGroup.from_dict(cluster_addon_model_cache_node_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


