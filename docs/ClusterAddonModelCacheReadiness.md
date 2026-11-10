# ClusterAddonModelCacheReadiness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_trust_subject** | **str** | The Kubernetes service account the weight cache downloads as, to grant access to in your cloud IAM. | [optional] 
**credential_secret_name** | **str** | The Secret the cluster&#39;s models read private artifacts with. | [optional] 
**credential_secret_namespace** | **str** | The namespace that Secret must exist in. | [optional] 
**enabled** | **bool** | Whether the cache is turned on at all. | [optional] 
**identity_annotations** | **Dict[str, str]** | The cloud workload-identity annotations the add-on binds its models, and its cache&#39;s downloads, to. Absent when the add-on has no identity. | [optional] 
**models_trust_subject** | **str** | The Kubernetes service account pattern to grant access to in your cloud IAM, covering every model on this cluster. | [optional] 
**node_groups** | [**List[ClusterAddonModelCacheNodeGroup]**](ClusterAddonModelCacheNodeGroup.md) | The node groups holding the cache: each node group whose disk is known, and the cluster&#39;s GPU node pool when it has one. | [optional] 
**node_storage_path** | **str** | The directory on each cached node the weights are held in, the same path serving containers read them from. | [optional] 
**summary** | **str** | Says in plain words where the cache holds the weights. Empty when the cache is off. | [optional] 
**warning** | **str** | Says what the cache cannot do here. Empty when nothing is wrong. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_model_cache_readiness import ClusterAddonModelCacheReadiness

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonModelCacheReadiness from a JSON string
cluster_addon_model_cache_readiness_instance = ClusterAddonModelCacheReadiness.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonModelCacheReadiness.to_json())

# convert the object into a dict
cluster_addon_model_cache_readiness_dict = cluster_addon_model_cache_readiness_instance.to_dict()
# create an instance of ClusterAddonModelCacheReadiness from a dict
cluster_addon_model_cache_readiness_from_dict = ClusterAddonModelCacheReadiness.from_dict(cluster_addon_model_cache_readiness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


