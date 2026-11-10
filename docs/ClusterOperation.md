# ClusterOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_node_groups** | **List[str]** | The node groups the operation adds, which the cluster does not have yet; they are in nodeGroups too. | [optional] 
**attempt** | **int** | The attempt number of the step running now. Omitted when unknown. | [optional] 
**involves_control_plane** | **bool** | True when the operation changes the control plane. | [optional] 
**kind** | [**ClusterOperationKind**](ClusterOperationKind.md) | The operation running on the cluster. | [optional] 
**node_groups** | **List[str]** | The node groups the operation adds, changes or removes. | [optional] 
**phase_label** | **str** | The step the operation is on in words, such as Creating node groups. Omitted when the operation names no step. | [optional] 
**started_at** | **datetime** | When the operation started. | [optional] 
**step** | [**ClusterOperationStep**](ClusterOperationStep.md) | The step the operation is on. Omitted before its first step. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_operation import ClusterOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperation from a JSON string
cluster_operation_instance = ClusterOperation.from_json(json)
# print the JSON string representation of the object
print(ClusterOperation.to_json())

# convert the object into a dict
cluster_operation_dict = cluster_operation_instance.to_dict()
# create an instance of ClusterOperation from a dict
cluster_operation_from_dict = ClusterOperation.from_dict(cluster_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


