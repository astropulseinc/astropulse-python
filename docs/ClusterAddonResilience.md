# ClusterAddonResilience


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**AddonAvailability**](AddonAvailability.md) | The effective setting: Standard when none was applied. | [optional] 
**per_node** | **str** | Names the nodes the main component runs one copy on, such as \&quot;GPU node\&quot;; Replicas is then how many run now, 0 when not yet known. | [optional] 
**reason** | **str** | Says why that many copies run, such as \&quot;1 replica: the cluster has fewer than two nodes it can run on\&quot;. | [optional] 
**replicas** | **int** | How many copies of the add-on&#39;s most available component run. | [optional] 
**resources** | [**AddonResources**](AddonResources.md) | The main component&#39;s effective sizing. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_resilience import ClusterAddonResilience

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonResilience from a JSON string
cluster_addon_resilience_instance = ClusterAddonResilience.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonResilience.to_json())

# convert the object into a dict
cluster_addon_resilience_dict = cluster_addon_resilience_instance.to_dict()
# create an instance of ClusterAddonResilience from a dict
cluster_addon_resilience_from_dict = ClusterAddonResilience.from_dict(cluster_addon_resilience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


