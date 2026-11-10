# WorkloadScanFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_count** | **int** | How many scanned containers this workload has — at least len(Images), and more when containers share an image. | [optional] 
**counts** | [**ScanFindingsSeverityCounts**](ScanFindingsSeverityCounts.md) | Totals over the DISTINCT images in Images, and so equal the sum of their counts exactly. Not a per-container sum: an image running in three containers contributes its findings once. | [optional] 
**images** | [**List[ImageScanFinding]**](ImageScanFinding.md) | The per-image breakdown Counts is built from. It is omitted when an image breakdown is unavailable. | [optional] 
**kind** | [**WorkloadKind**](WorkloadKind.md) | The kind of Kubernetes object that runs the workload; absent for one the API does not define. | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**owner** | [**ScanFindingOwner**](ScanFindingOwner.md) | Identifies the application or add-on associated with this workload. It is absent when no public association is known. | [optional] 

## Example

```python
from astropulse._generated.models.workload_scan_finding import WorkloadScanFinding

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadScanFinding from a JSON string
workload_scan_finding_instance = WorkloadScanFinding.from_json(json)
# print the JSON string representation of the object
print(WorkloadScanFinding.to_json())

# convert the object into a dict
workload_scan_finding_dict = workload_scan_finding_instance.to_dict()
# create an instance of WorkloadScanFinding from a dict
workload_scan_finding_from_dict = WorkloadScanFinding.from_dict(workload_scan_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


