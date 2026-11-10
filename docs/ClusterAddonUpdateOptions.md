# ClusterAddonUpdateOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Validates the request and changes nothing. | [optional] 
**strategy** | [**ClusterAddonUpdateStrategy**](ClusterAddonUpdateStrategy.md) | How replacements are rolled out. | [optional] 
**timeout** | **str** | Bounds that wait, as a duration (\&quot;10m\&quot;). | [optional] 
**wait_for_ready** | **bool** | The request open until the update has settled. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_update_options import ClusterAddonUpdateOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonUpdateOptions from a JSON string
cluster_addon_update_options_instance = ClusterAddonUpdateOptions.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonUpdateOptions.to_json())

# convert the object into a dict
cluster_addon_update_options_dict = cluster_addon_update_options_instance.to_dict()
# create an instance of ClusterAddonUpdateOptions from a dict
cluster_addon_update_options_from_dict = ClusterAddonUpdateOptions.from_dict(cluster_addon_update_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


