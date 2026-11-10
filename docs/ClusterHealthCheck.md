# ClusterHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issues** | **List[str]** |  | [optional] 
**nodes_not_ready** | **int** |  | [optional] 
**nodes_ready** | **int** |  | [optional] 
**system_pods_health** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_health_check import ClusterHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHealthCheck from a JSON string
cluster_health_check_instance = ClusterHealthCheck.from_json(json)
# print the JSON string representation of the object
print(ClusterHealthCheck.to_json())

# convert the object into a dict
cluster_health_check_dict = cluster_health_check_instance.to_dict()
# create an instance of ClusterHealthCheck from a dict
cluster_health_check_from_dict = ClusterHealthCheck.from_dict(cluster_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


