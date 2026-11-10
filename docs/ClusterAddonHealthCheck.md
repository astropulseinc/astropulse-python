# ClusterAddonHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle** | **bool** | True when the check passes because there is nothing for it to check yet. An idle check always has a message saying what is missing. | [optional] 
**message** | **str** | Says what was found, when passing alone does not explain it. | [optional] 
**name** | **str** | What was checked. | [optional] 
**next_step** | [**NextStep**](NextStep.md) | The one thing to do about a check that failed, when there is one. | [optional] 
**passing** | **bool** | Whether it passed. | [optional] 
**pending** | **bool** | True when the check has not passed because what it checks is still starting or waiting, not because something is wrong. A pending check always has a message: one complete sentence saying what it waits for. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_health_check import ClusterAddonHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonHealthCheck from a JSON string
cluster_addon_health_check_instance = ClusterAddonHealthCheck.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonHealthCheck.to_json())

# convert the object into a dict
cluster_addon_health_check_dict = cluster_addon_health_check_instance.to_dict()
# create an instance of ClusterAddonHealthCheck from a dict
cluster_addon_health_check_from_dict = ClusterAddonHealthCheck.from_dict(cluster_addon_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


