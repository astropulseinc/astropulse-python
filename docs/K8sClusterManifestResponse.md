# K8sClusterManifestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**K8sClusterManifest**](K8sClusterManifest.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster_manifest_response import K8sClusterManifestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterManifestResponse from a JSON string
k8s_cluster_manifest_response_instance = K8sClusterManifestResponse.from_json(json)
# print the JSON string representation of the object
print(K8sClusterManifestResponse.to_json())

# convert the object into a dict
k8s_cluster_manifest_response_dict = k8s_cluster_manifest_response_instance.to_dict()
# create an instance of K8sClusterManifestResponse from a dict
k8s_cluster_manifest_response_from_dict = K8sClusterManifestResponse.from_dict(k8s_cluster_manifest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


