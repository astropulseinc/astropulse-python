# ClusterAddonSupport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated_on** | **date** | The date this version was deprecated, as YYYY-MM-DD. | [optional] 
**end_of_support** | **date** | The date this version is retired, as YYYY-MM-DD. | [optional] 
**recommended** | **str** | The version to move to. Empty when this is the recommended version. | [optional] 
**status** | [**ClusterAddonSupportStatus**](ClusterAddonSupportStatus.md) | Where the version is in its support lifecycle. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_support import ClusterAddonSupport

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonSupport from a JSON string
cluster_addon_support_instance = ClusterAddonSupport.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonSupport.to_json())

# convert the object into a dict
cluster_addon_support_dict = cluster_addon_support_instance.to_dict()
# create an instance of ClusterAddonSupport from a dict
cluster_addon_support_from_dict = ClusterAddonSupport.from_dict(cluster_addon_support_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


