# K8sClusterUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The API version. Must be \&quot;platform.astropulse.io/v1\&quot; when provided. | [optional] 
**kind** | **str** | The resource kind. Must be \&quot;K8sClusterUpdate\&quot; when provided. | [optional] 
**spec** | [**UpdateClusterSpec**](UpdateClusterSpec.md) | Contains the cluster update parameters. | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster_update import K8sClusterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterUpdate from a JSON string
k8s_cluster_update_instance = K8sClusterUpdate.from_json(json)
# print the JSON string representation of the object
print(K8sClusterUpdate.to_json())

# convert the object into a dict
k8s_cluster_update_dict = k8s_cluster_update_instance.to_dict()
# create an instance of K8sClusterUpdate from a dict
k8s_cluster_update_from_dict = K8sClusterUpdate.from_dict(k8s_cluster_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


