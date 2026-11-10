# ClusterStorageBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** | The StorageClass the name refers to. It must be one the cluster has. | 
**kind** | [**StorageKind**](StorageKind.md) | What the storage provides. Required when AstroPulse does not recognize the class&#39;s driver; otherwise it is filled in and cannot disagree with what the driver provides. | [optional] 
**name** | **str** | The name to use for this storage. A lowercase DNS label. | 
**state** | [**StorageBindingState**](StorageBindingState.md) | Whether the class is on the cluster. Read-only. | [optional] 
**used_by** | [**List[ClusterStorageBindingUse]**](ClusterStorageBindingUse.md) | The installed add-on settings that ask for this name. A name in use cannot be unbound or pointed at another class. Read-only. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_storage_binding import ClusterStorageBinding

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStorageBinding from a JSON string
cluster_storage_binding_instance = ClusterStorageBinding.from_json(json)
# print the JSON string representation of the object
print(ClusterStorageBinding.to_json())

# convert the object into a dict
cluster_storage_binding_dict = cluster_storage_binding_instance.to_dict()
# create an instance of ClusterStorageBinding from a dict
cluster_storage_binding_from_dict = ClusterStorageBinding.from_dict(cluster_storage_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


