# ClusterCloudIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubelet_identity_object_id** | **str** | The object ID of the AKS kubelet identity, which image pulls use. | [optional] 
**node_roles** | [**List[NodeRole]**](NodeRole.md) | The identities the cluster&#39;s nodes run as: one per node group on EKS, plus one for Karpenter&#39;s nodes; on GKE and AKS one for all nodes, or one per node pool when GKE pools differ. | [optional] 
**node_service_account** | **str** | The service account GKE nodes run as. | [optional] 
**oidc_issuer_url** | **str** | The cluster&#39;s OIDC issuer (EKS, AKS), for workload identity trust. | [optional] 
**workload_identity_pool** | **str** | The GKE workload identity pool, &lt;project&gt;.svc.id.goog. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_cloud_identity import ClusterCloudIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCloudIdentity from a JSON string
cluster_cloud_identity_instance = ClusterCloudIdentity.from_json(json)
# print the JSON string representation of the object
print(ClusterCloudIdentity.to_json())

# convert the object into a dict
cluster_cloud_identity_dict = cluster_cloud_identity_instance.to_dict()
# create an instance of ClusterCloudIdentity from a dict
cluster_cloud_identity_from_dict = ClusterCloudIdentity.from_dict(cluster_cloud_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


