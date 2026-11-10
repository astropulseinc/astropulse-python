# ClusterAddonTLSMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Reports whether applications on the cluster can use the mode. | [optional] 
**mode** | [**TLSMode**](TLSMode.md) | The TLS mode. | [optional] 
**needs** | **str** | The step that makes the mode available; empty when it is. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_tls_mode import ClusterAddonTLSMode

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonTLSMode from a JSON string
cluster_addon_tls_mode_instance = ClusterAddonTLSMode.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonTLSMode.to_json())

# convert the object into a dict
cluster_addon_tls_mode_dict = cluster_addon_tls_mode_instance.to_dict()
# create an instance of ClusterAddonTLSMode from a dict
cluster_addon_tls_mode_from_dict = ClusterAddonTLSMode.from_dict(cluster_addon_tls_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


