# ClusterAddonHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**List[ClusterAddonHealthCheck]**](ClusterAddonHealthCheck.md) | The individual results behind Healthy. | [optional] 
**healthy** | **bool** | The single answer: is the add-on&#39;s own workload working? | [optional] 
**last_checked** | **str** | When the cluster last reported, RFC 3339. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Say what the add-on&#39;s current health stops on the cluster, each with the one step to take. | [optional] 
**overall_status** | [**ClusterAddonStatus**](ClusterAddonStatus.md) | Summarises the checks below in one word. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_health import ClusterAddonHealth

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonHealth from a JSON string
cluster_addon_health_instance = ClusterAddonHealth.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonHealth.to_json())

# convert the object into a dict
cluster_addon_health_dict = cluster_addon_health_instance.to_dict()
# create an instance of ClusterAddonHealth from a dict
cluster_addon_health_from_dict = ClusterAddonHealth.from_dict(cluster_addon_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


