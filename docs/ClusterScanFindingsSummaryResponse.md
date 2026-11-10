# ClusterScanFindingsSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterScanFindingsSummary**](ClusterScanFindingsSummary.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_scan_findings_summary_response import ClusterScanFindingsSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterScanFindingsSummaryResponse from a JSON string
cluster_scan_findings_summary_response_instance = ClusterScanFindingsSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterScanFindingsSummaryResponse.to_json())

# convert the object into a dict
cluster_scan_findings_summary_response_dict = cluster_scan_findings_summary_response_instance.to_dict()
# create an instance of ClusterScanFindingsSummaryResponse from a dict
cluster_scan_findings_summary_response_from_dict = ClusterScanFindingsSummaryResponse.from_dict(cluster_scan_findings_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


