# K8sClusterListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[K8sCluster]**](K8sCluster.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster_list_response import K8sClusterListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterListResponse from a JSON string
k8s_cluster_list_response_instance = K8sClusterListResponse.from_json(json)
# print the JSON string representation of the object
print(K8sClusterListResponse.to_json())

# convert the object into a dict
k8s_cluster_list_response_dict = k8s_cluster_list_response_instance.to_dict()
# create an instance of K8sClusterListResponse from a dict
k8s_cluster_list_response_from_dict = K8sClusterListResponse.from_dict(k8s_cluster_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


