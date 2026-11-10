# K8sClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The cluster name (required, 1-50 characters, valid DNS name). Format: lowercase alphanumeric and hyphens, must start with a letter. | 
**cluster_spec** | [**K8sClusterSpec**](K8sClusterSpec.md) | The cluster specification containing control plane and data plane configuration (required) | 
**provider** | [**Provider**](Provider.md) | The cloud provider (required). One of: aws, azure, gcp. | 
**provisioner** | [**Provisioner**](Provisioner.md) | The provisioner configuration specifying which cloud provider and settings to use (required) | 
**region** | **str** | The cloud provider region (required, minimum 1 character). Provider-specific format: AWS (e.g. \&quot;us-west-2\&quot;), GCP (e.g. \&quot;us-central1\&quot;), Azure (e.g. \&quot;eastus\&quot;). | 

## Example

```python
from astropulse._generated.models.k8s_cluster_request import K8sClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterRequest from a JSON string
k8s_cluster_request_instance = K8sClusterRequest.from_json(json)
# print the JSON string representation of the object
print(K8sClusterRequest.to_json())

# convert the object into a dict
k8s_cluster_request_dict = k8s_cluster_request_instance.to_dict()
# create an instance of K8sClusterRequest from a dict
k8s_cluster_request_from_dict = K8sClusterRequest.from_dict(k8s_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


