# ClusterAddonCatalogEntryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClusterAddonCatalogEntry]**](ClusterAddonCatalogEntry.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_catalog_entry_list_response import ClusterAddonCatalogEntryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonCatalogEntryListResponse from a JSON string
cluster_addon_catalog_entry_list_response_instance = ClusterAddonCatalogEntryListResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonCatalogEntryListResponse.to_json())

# convert the object into a dict
cluster_addon_catalog_entry_list_response_dict = cluster_addon_catalog_entry_list_response_instance.to_dict()
# create an instance of ClusterAddonCatalogEntryListResponse from a dict
cluster_addon_catalog_entry_list_response_from_dict = ClusterAddonCatalogEntryListResponse.from_dict(cluster_addon_catalog_entry_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


