# NodeRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**NodeRoleKind**](NodeRoleKind.md) | What the nodes are: an EKS managed node group, Karpenter&#39;s nodes, GKE nodes or AKS kubelets. | [optional] 
**label** | **str** | The name to show for the nodes that run as this identity, such as the node group&#39;s name. | [optional] 
**node_group** | **str** | The node group whose nodes run as this identity; empty when the identity is not one node group&#39;s. | [optional] 
**role_arn** | **str** | The ARN of the IAM role the nodes run as (EKS). | [optional] 
**role_name** | **str** | The identity&#39;s name: the IAM role (EKS), the service account&#39;s email (GKE) or the managed identity (AKS). | [optional] 

## Example

```python
from astropulse._generated.models.node_role import NodeRole

# TODO update the JSON string below
json = "{}"
# create an instance of NodeRole from a JSON string
node_role_instance = NodeRole.from_json(json)
# print the JSON string representation of the object
print(NodeRole.to_json())

# convert the object into a dict
node_role_dict = node_role_instance.to_dict()
# create an instance of NodeRole from a dict
node_role_from_dict = NodeRole.from_dict(node_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


