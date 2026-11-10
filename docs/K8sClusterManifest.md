# K8sClusterManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The API version. Must be \&quot;platform.astropulse.io/v1\&quot; when provided. | [optional] 
**kind** | **str** | The resource kind. Must be \&quot;K8sCluster\&quot; when provided. | [optional] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) | The optional manifest metadata block. When metadata.name is set and spec.clusterName is omitted, metadata.name is used as the cluster name. | [optional] 
**spec** | [**K8sClusterRequest**](K8sClusterRequest.md) | Contains the cluster creation parameters. | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster_manifest import K8sClusterManifest

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterManifest from a JSON string
k8s_cluster_manifest_instance = K8sClusterManifest.from_json(json)
# print the JSON string representation of the object
print(K8sClusterManifest.to_json())

# convert the object into a dict
k8s_cluster_manifest_dict = k8s_cluster_manifest_instance.to_dict()
# create an instance of K8sClusterManifest from a dict
k8s_cluster_manifest_from_dict = K8sClusterManifest.from_dict(k8s_cluster_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


