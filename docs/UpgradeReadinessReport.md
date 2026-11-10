# UpgradeReadinessReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_proceed** | **bool** | Indicates whether the upgrade can safely proceed | [optional] 
**cluster_health** | [**ClusterHealthCheck**](ClusterHealthCheck.md) | The current cluster health assessment; absent when not evaluated. | [optional] 
**critical_issues** | [**List[ValidationIssue]**](ValidationIssue.md) | Blocking issues that must be resolved before upgrading | [optional] 
**estimated_time** | **str** | The estimated upgrade duration (e.g. \&quot;45-60 minutes\&quot;) | [optional] 
**not_evaluated** | [**List[ReadinessReportSection]**](ReadinessReportSection.md) | Names the analysis sections this report does not include. | [optional] 
**nothing_to_upgrade** | **bool** | True when the cluster is already at the newest version the requested target resolves to, so there is no upgrade to perform. | [optional] 
**nothing_to_upgrade_summary** | **str** | The message to show when nothingToUpgrade is true; empty otherwise. | [optional] 
**readiness_score** | **int** | The overall readiness score (0-100, higher is better); absent when the report did not assess readiness. | [optional] 
**recommendations** | **List[str]** | Suggested actions to improve upgrade safety | [optional] 
**report_summary** | **str** | A human-readable summary of the readiness analysis | [optional] 
**resource_analysis** | [**ResourceCapacityCheck**](ResourceCapacityCheck.md) | Contains resource capacity validation; absent when not evaluated. | [optional] 
**risk_level** | [**UpgradeRiskLevel**](UpgradeRiskLevel.md) | The assessed risk, Unknown when the report did not assess readiness. | [optional] 
**version_analysis** | [**K8sVersionAnalysis**](K8sVersionAnalysis.md) | Contains Kubernetes version compatibility analysis; absent when not evaluated. | [optional] 
**warnings** | [**List[ValidationIssue]**](ValidationIssue.md) | Non-blocking issues to be aware of | [optional] 
**workload_analysis** | [**WorkloadImpactAnalysis**](WorkloadImpactAnalysis.md) | Contains workload impact assessment; absent when not evaluated. | [optional] 

## Example

```python
from astropulse._generated.models.upgrade_readiness_report import UpgradeReadinessReport

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeReadinessReport from a JSON string
upgrade_readiness_report_instance = UpgradeReadinessReport.from_json(json)
# print the JSON string representation of the object
print(UpgradeReadinessReport.to_json())

# convert the object into a dict
upgrade_readiness_report_dict = upgrade_readiness_report_instance.to_dict()
# create an instance of UpgradeReadinessReport from a dict
upgrade_readiness_report_from_dict = UpgradeReadinessReport.from_dict(upgrade_readiness_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


