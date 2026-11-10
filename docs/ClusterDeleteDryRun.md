# ClusterDeleteDryRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The cluster the delete was asked for. | [optional] 
**groups** | [**List[ClusterDeleteGroup]**](ClusterDeleteGroup.md) | What the delete would act on, by kind, the groups needing your attention first. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Say what the delete would leave and what to do about it. | [optional] 
**summary** | **str** | One line naming, by kind, what the delete would act on. | [optional] 
**title** | **str** | The verdict as a headline to show. | 
**verdict** | [**DryRunVerdict**](DryRunVerdict.md) | How the dry run ended: Passed when the delete would go ahead and every group was listed, Unfinished when a group could not be listed. | 

## Example

```python
from astropulse._generated.models.cluster_delete_dry_run import ClusterDeleteDryRun

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDeleteDryRun from a JSON string
cluster_delete_dry_run_instance = ClusterDeleteDryRun.from_json(json)
# print the JSON string representation of the object
print(ClusterDeleteDryRun.to_json())

# convert the object into a dict
cluster_delete_dry_run_dict = cluster_delete_dry_run_instance.to_dict()
# create an instance of ClusterDeleteDryRun from a dict
cluster_delete_dry_run_from_dict = ClusterDeleteDryRun.from_dict(cluster_delete_dry_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


