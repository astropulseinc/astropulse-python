# UpdateNodeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | [**AcceleratorAttachment**](AcceleratorAttachment.md) | Optional for update patches, with patch semantics distinct from a plain optional field. Omit it to leave the stored accelerator unchanged. Send an empty message ({}) to clear it — a material change that recreates the node group, which must then carry machineTypes. Send a populated union member to replace it, which also recreates the group. | [optional] 
**availability_zones** | **List[str]** | Optional for update patches. When omitted, the server preserves the existing value. | [optional] 
**disk_size_gb** | **int** | The desired root disk for the group&#39;s nodes, in whole gigabytes. Omitted, the group keeps the size it has; changing it replaces the group&#39;s nodes, and is refused on gke. | [optional] 
**instance_type** | [**InstanceType**](InstanceType.md) | Optional for update patches. When omitted, the server preserves the existing value. | [optional] 
**labels** | **Dict[str, str]** | The group&#39;s Kubernetes node labels (optional); omitted, the group keeps its labels. Keys are Kubernetes label keys, not under kubernetes.io or k8s.io (at most 63 characters in all on eks); values are 1-63 letters, digits, &#39;-&#39;, &#39;_&#39; and &#39;.&#39;, starting and ending with a letter or digit. | [optional] 
**machine_types** | **List[str]** | Optional for update patches. When omitted, the server preserves the existing value. | [optional] 
**max_node** | **int** | The desired maximum node count for the node group. Nil means \&quot;leave as it is\&quot; — see MinNode. | [optional] 
**min_node** | **int** | The desired minimum node count for the node group.  A pointer so that an omitted field stays distinguishable from an explicit zero: since a group may legitimately have a floor of zero, decoding an absent minNode to 0 would turn every partial patch into a scale-to-zero request. Nil means \&quot;leave as it is\&quot; and is filled in from the stored cluster by mergeNodeGroupDefaults. | [optional] 
**name** | **str** | The existing node group name to update. | 
**taints** | [**List[Tainted]**](Tainted.md) | Optional taints to apply. | [optional] 

## Example

```python
from astropulse._generated.models.update_node_group import UpdateNodeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNodeGroup from a JSON string
update_node_group_instance = UpdateNodeGroup.from_json(json)
# print the JSON string representation of the object
print(UpdateNodeGroup.to_json())

# convert the object into a dict
update_node_group_dict = update_node_group_instance.to_dict()
# create an instance of UpdateNodeGroup from a dict
update_node_group_from_dict = UpdateNodeGroup.from_dict(update_node_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


