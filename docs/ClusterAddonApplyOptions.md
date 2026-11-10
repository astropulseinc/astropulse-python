# ClusterAddonApplyOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Validates the apply and changes nothing. | [optional] 
**timeout** | **str** | Bounds that wait, as a duration (\&quot;10m\&quot;). | [optional] 
**wait_for_ready** | **bool** | Waits until the add-on is serving before the apply returns. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_apply_options import ClusterAddonApplyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonApplyOptions from a JSON string
cluster_addon_apply_options_instance = ClusterAddonApplyOptions.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonApplyOptions.to_json())

# convert the object into a dict
cluster_addon_apply_options_dict = cluster_addon_apply_options_instance.to_dict()
# create an instance of ClusterAddonApplyOptions from a dict
cluster_addon_apply_options_from_dict = ClusterAddonApplyOptions.from_dict(cluster_addon_apply_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


