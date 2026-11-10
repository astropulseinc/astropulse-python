# ClusterUpdateDryRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The unique cluster identifier | [optional] 
**errors** | **List[str]** | Contains validation error messages that block the update. | [optional] 
**message** | **str** | Provides human-readable details about the result | [optional] 
**notices** | [**List[Notice]**](Notice.md) | What the update will do, what an update sent with replaceRunning does, and warnings about the cluster it leaves; a warning doesn&#39;t stop the update. | [optional] 
**outcome** | [**Outcome**](Outcome.md) | The decision on the update: Proceed, or Blocked when a check failed or did not finish. | [optional] 
**status** | [**ClusterStatus**](ClusterStatus.md) | The cluster&#39;s current status. | [optional] 
**title** | **str** | The verdict as a headline to show. | 
**upgrade_plan** | [**UpgradePlan**](UpgradePlan.md) | Describes the phased execution plan | [optional] 
**upgrade_report** | [**UpgradeReadinessReport**](UpgradeReadinessReport.md) | Contains a comprehensive readiness analysis (present when generateReport is true) | [optional] 
**validation_passed** | **bool** | True when every check finished and none failed. | [optional] 
**verdict** | [**DryRunVerdict**](DryRunVerdict.md) | How the dry run ended. | 

## Example

```python
from astropulse._generated.models.cluster_update_dry_run import ClusterUpdateDryRun

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterUpdateDryRun from a JSON string
cluster_update_dry_run_instance = ClusterUpdateDryRun.from_json(json)
# print the JSON string representation of the object
print(ClusterUpdateDryRun.to_json())

# convert the object into a dict
cluster_update_dry_run_dict = cluster_update_dry_run_instance.to_dict()
# create an instance of ClusterUpdateDryRun from a dict
cluster_update_dry_run_from_dict = ClusterUpdateDryRun.from_dict(cluster_update_dry_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


