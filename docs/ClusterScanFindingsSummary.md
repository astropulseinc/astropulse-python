# ClusterScanFindingsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_seconds** | **int** | Computed at read time from ReportedAt: how long ago the scan completed. | [optional] 
**cluster_name** | **str** |  | [optional] 
**no_result** | [**List[ScanFindingsNoResult]**](ScanFindingsNoResult.md) | Lists every application and installed add-on on the cluster that has no scan result, with the reason for each. | [optional] 
**notes** | **List[str]** | Plain sentences about what these results leave out, such as findings left out by platform policy. Absent when there is nothing to say. | [optional] 
**received_at** | **str** | When AstroPulse ingested this snapshot. | [optional] 
**reported_at** | **str** | When the scan completed. | [optional] 
**unscanned_images** | [**List[ScanFindingsUnscannedImages]**](ScanFindingsUnscannedImages.md) | The images the scanner could not scan, grouped by reason. Absent when every scan left a result. | [optional] 
**workloads** | [**List[WorkloadScanFinding]**](WorkloadScanFinding.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_scan_findings_summary import ClusterScanFindingsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterScanFindingsSummary from a JSON string
cluster_scan_findings_summary_instance = ClusterScanFindingsSummary.from_json(json)
# print the JSON string representation of the object
print(ClusterScanFindingsSummary.to_json())

# convert the object into a dict
cluster_scan_findings_summary_dict = cluster_scan_findings_summary_instance.to_dict()
# create an instance of ClusterScanFindingsSummary from a dict
cluster_scan_findings_summary_from_dict = ClusterScanFindingsSummary.from_dict(cluster_scan_findings_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


