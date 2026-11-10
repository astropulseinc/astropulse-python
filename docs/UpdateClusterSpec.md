# UpdateClusterSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aks** | [**AKSUpdateSpec**](AKSUpdateSpec.md) | The specification for aks-specific updates (optional, for aks clusters only) | [optional] 
**eks** | [**EKSUpdateSpec**](EKSUpdateSpec.md) | Provider-specific update configurations (optional, at most one should be set matching your cluster&#39;s provisioner) EKS is the specification for eks-specific updates (optional, for eks clusters only) | [optional] 
**gke** | [**GKEUpdateSpec**](GKEUpdateSpec.md) | The specification for gke-specific updates (optional, for gke clusters only) | [optional] 
**kubernetes_version** | **str** | The target Kubernetes version (optional). For upgrade: must be at most 1 minor version above current. For rollback: set allowDowngrade&#x3D;true in updateConfig. | [optional] 
**node_groups** | [**List[UpdateNodeGroup]**](UpdateNodeGroup.md) | Specifies node groups to update (optional). Each entry patches an existing node group by name. Omitted fields are merged from the stored cluster definition — no need to repeat unchanged values. | [optional] 
**remove_node_groups** | **List[str]** | Names the node groups to remove from the cluster (optional). Each group&#39;s nodes are drained, then the group is deleted. | [optional] 
**self_hosted** | [**SelfHostedUpdateSpec**](SelfHostedUpdateSpec.md) | The specification for selfHosted cluster updates (optional, for selfHosted clusters only) | [optional] 
**tags** | **Dict[str, str]** | Replace the cluster&#39;s cloud tags (labels on GKE) with this set, following its provider&#39;s create rule; omitted keeps them and an empty map removes them. Tags AstroPulse and the cloud write are kept, and self-hosted clusters take none. | [optional] 
**update_config** | [**UpdateConfig**](UpdateConfig.md) | Provides safety and rollback controls for the update operation (optional). | [optional] 

## Example

```python
from astropulse._generated.models.update_cluster_spec import UpdateClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterSpec from a JSON string
update_cluster_spec_instance = UpdateClusterSpec.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterSpec.to_json())

# convert the object into a dict
update_cluster_spec_dict = update_cluster_spec_instance.to_dict()
# create an instance of UpdateClusterSpec from a dict
update_cluster_spec_from_dict = UpdateClusterSpec.from_dict(update_cluster_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


