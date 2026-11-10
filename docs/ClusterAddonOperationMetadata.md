# ClusterAddonOperationMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warning** | **str** | Something that succeeded but is worth reading. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_operation_metadata import ClusterAddonOperationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonOperationMetadata from a JSON string
cluster_addon_operation_metadata_instance = ClusterAddonOperationMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonOperationMetadata.to_json())

# convert the object into a dict
cluster_addon_operation_metadata_dict = cluster_addon_operation_metadata_instance.to_dict()
# create an instance of ClusterAddonOperationMetadata from a dict
cluster_addon_operation_metadata_from_dict = ClusterAddonOperationMetadata.from_dict(cluster_addon_operation_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


