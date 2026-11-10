# ClusterStorageBindingUse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_type** | [**ClusterAddonType**](ClusterAddonType.md) | The add-on whose setting asks for the name. | [optional] 
**setting** | **str** | The setting&#39;s path in the add-on&#39;s configuration, such as &#x60;prometheus.storage.name&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_storage_binding_use import ClusterStorageBindingUse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStorageBindingUse from a JSON string
cluster_storage_binding_use_instance = ClusterStorageBindingUse.from_json(json)
# print the JSON string representation of the object
print(ClusterStorageBindingUse.to_json())

# convert the object into a dict
cluster_storage_binding_use_dict = cluster_storage_binding_use_instance.to_dict()
# create an instance of ClusterStorageBindingUse from a dict
cluster_storage_binding_use_from_dict = ClusterStorageBindingUse.from_dict(cluster_storage_binding_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


