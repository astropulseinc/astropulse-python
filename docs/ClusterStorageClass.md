# ClusterStorageClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_volume_expansion** | **bool** | Reports whether volumes of this class can grow. | [optional] 
**binding_mode** | **str** | When a volume is provisioned: Immediate, or WaitForFirstConsumer to wait for the pod that uses it. | [optional] 
**is_default** | **bool** | Reports whether a volume claim that names no class uses this one. | [optional] 
**kind** | [**StorageKind**](StorageKind.md) | What this class provides. Absent when AstroPulse does not recognize the class&#39;s driver; a binding to it then declares its &#x60;kind&#x60;. | [optional] 
**name** | **str** | The StorageClass name. | [optional] 
**provisioner** | **str** | The CSI driver the class uses. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_storage_class import ClusterStorageClass

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStorageClass from a JSON string
cluster_storage_class_instance = ClusterStorageClass.from_json(json)
# print the JSON string representation of the object
print(ClusterStorageClass.to_json())

# convert the object into a dict
cluster_storage_class_dict = cluster_storage_class_instance.to_dict()
# create an instance of ClusterStorageClass from a dict
cluster_storage_class_from_dict = ClusterStorageClass.from_dict(cluster_storage_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


