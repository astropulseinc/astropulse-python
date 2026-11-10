# ClusterDryRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**List[PreflightCheck]**](PreflightCheck.md) | The checks a create runs before it starts, the account connection first. A check whose status is Fail carries its fix in remediation; Warn does not block. | [optional] 
**complete** | **bool** | False when some checks did not finish; unfinishedChecks names them and the dry run should be run again. | [optional] 
**message** | **str** | The verdict in words; it names each failed check and its fix, and any check that did not finish. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Warnings about the cluster the create would make; they don&#39;t stop it. | [optional] 
**resolved_node_groups** | [**List[ResolvedNodeGroup]**](ResolvedNodeGroup.md) | The node groups that named an accelerator but no machine type, with the machine types AstroPulse chose for them, in name order. | [optional] 
**title** | **str** | The verdict as a headline to show. | 
**unfinished_checks** | **List[str]** | The checks that did not finish, so they neither passed nor failed. | [optional] 
**valid** | **bool** | True when every check finished and none failed, so a create with the same body would start. | [optional] 
**verdict** | [**DryRunVerdict**](DryRunVerdict.md) | How the dry run ended. | 

## Example

```python
from astropulse._generated.models.cluster_dry_run import ClusterDryRun

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDryRun from a JSON string
cluster_dry_run_instance = ClusterDryRun.from_json(json)
# print the JSON string representation of the object
print(ClusterDryRun.to_json())

# convert the object into a dict
cluster_dry_run_dict = cluster_dry_run_instance.to_dict()
# create an instance of ClusterDryRun from a dict
cluster_dry_run_from_dict = ClusterDryRun.from_dict(cluster_dry_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


