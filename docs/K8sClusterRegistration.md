# K8sClusterRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The API version. Must be \&quot;platform.astropulse.io/v1\&quot; when provided. | [optional] 
**kind** | **str** | The resource kind. Must be \&quot;K8sClusterRegistration\&quot; when provided. | [optional] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) | The optional manifest metadata block. When metadata.name is set and spec.clusterName is omitted, metadata.name is used as the cluster name. | [optional] 
**spec** | [**RegisterClusterRequest**](RegisterClusterRequest.md) | The registration specification. | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster_registration import K8sClusterRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterRegistration from a JSON string
k8s_cluster_registration_instance = K8sClusterRegistration.from_json(json)
# print the JSON string representation of the object
print(K8sClusterRegistration.to_json())

# convert the object into a dict
k8s_cluster_registration_dict = k8s_cluster_registration_instance.to_dict()
# create an instance of K8sClusterRegistration from a dict
k8s_cluster_registration_from_dict = K8sClusterRegistration.from_dict(k8s_cluster_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


