# ClusterAddonSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthy** | **bool** | Whether the add-on&#39;s own workload is working; an add-on can be &#x60;Deployed&#x60; and still not healthy. Absent when its health was not read. | [optional] 
**message** | **str** | Explains the status in one sentence. | [optional] 
**next_step** | [**NextStep**](NextStep.md) | The one thing to do when the add-on has failed or is not healthy, the same step as notice.nextStep when there is a notice; absent otherwise. | [optional] 
**notice** | [**Notice**](Notice.md) | The add-on&#39;s statusNotice: what a failed or unhealthy status means and the one step that resolves it; absent otherwise. | [optional] 
**overall_status** | [**ClusterAddonStatus**](ClusterAddonStatus.md) | Summarises the add-on&#39;s health checks in one word, the same value as health.overallStatus on the add-on. | [optional] 
**status** | [**ClusterAddonStatus**](ClusterAddonStatus.md) | Whether the add-on is installed and working. | [optional] 
**type** | [**ClusterAddonType**](ClusterAddonType.md) | The add-on&#39;s public name, and what every add-on command takes. | [optional] 
**version** | **str** | The installed chart version. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_summary import ClusterAddonSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonSummary from a JSON string
cluster_addon_summary_instance = ClusterAddonSummary.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonSummary.to_json())

# convert the object into a dict
cluster_addon_summary_dict = cluster_addon_summary_instance.to_dict()
# create an instance of ClusterAddonSummary from a dict
cluster_addon_summary_from_dict = ClusterAddonSummary.from_dict(cluster_addon_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


