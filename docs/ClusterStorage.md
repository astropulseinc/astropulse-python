# ClusterStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindings** | [**List[ClusterStorageBinding]**](ClusterStorageBinding.md) | The names applications and add-ons use for storage. | [optional] 
**classes** | [**List[ClusterStorageClass]**](ClusterStorageClass.md) | The StorageClasses observed on the cluster. Read-only. | [optional] 
**kind_options** | [**SettingOptions**](SettingOptions.md) | The storage kinds a binding can declare: Shared, Dedicated or Node. | [optional] 
**observed_at** | **datetime** | When the classes were last observed, RFC 3339. Absent when the cluster&#39;s storage has not been observed yet, which is not the same as a cluster with no storage classes. | [optional] 
**observed_by** | [**StorageObserver**](StorageObserver.md) | What read the classes. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_storage import ClusterStorage

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStorage from a JSON string
cluster_storage_instance = ClusterStorage.from_json(json)
# print the JSON string representation of the object
print(ClusterStorage.to_json())

# convert the object into a dict
cluster_storage_dict = cluster_storage_instance.to_dict()
# create an instance of ClusterStorage from a dict
cluster_storage_from_dict = ClusterStorage.from_dict(cluster_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


