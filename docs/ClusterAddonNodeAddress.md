# ClusterAddonNodeAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ip** | **str** | The address reachable from outside it, empty when the node has none. | [optional] 
**internal_ip** | **str** | The address reachable from inside the cluster&#39;s network. | [optional] 
**node** | **str** | The node&#39;s name. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_node_address import ClusterAddonNodeAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonNodeAddress from a JSON string
cluster_addon_node_address_instance = ClusterAddonNodeAddress.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonNodeAddress.to_json())

# convert the object into a dict
cluster_addon_node_address_dict = cluster_addon_node_address_instance.to_dict()
# create an instance of ClusterAddonNodeAddress from a dict
cluster_addon_node_address_from_dict = ClusterAddonNodeAddress.from_dict(cluster_addon_node_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


