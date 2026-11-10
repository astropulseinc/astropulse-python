# ClusterSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | [**CloudProviderConfig**](CloudProviderConfig.md) | Specifies the cloud provider and region where the application will be deployed. | [optional] 
**cluster** | [**Cluster**](Cluster.md) | Specifies the cluster name where the application will be deployed. | [optional] 
**type** | [**ClusterSelectionType**](ClusterSelectionType.md) | Of cluster selection | [optional] 

## Example

```python
from astropulse._generated.models.cluster_selection import ClusterSelection

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSelection from a JSON string
cluster_selection_instance = ClusterSelection.from_json(json)
# print the JSON string representation of the object
print(ClusterSelection.to_json())

# convert the object into a dict
cluster_selection_dict = cluster_selection_instance.to_dict()
# create an instance of ClusterSelection from a dict
cluster_selection_from_dict = ClusterSelection.from_dict(cluster_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


