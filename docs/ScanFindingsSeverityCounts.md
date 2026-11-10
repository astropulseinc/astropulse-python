# ScanFindingsSeverityCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical** | **int** |  | [optional] 
**high** | **int** |  | [optional] 
**low** | **int** |  | [optional] 
**medium** | **int** |  | [optional] 
**var_none** | **int** | The scanner&#39;s informational bucket (no assigned severity). | [optional] 
**unknown** | **int** |  | [optional] 

## Example

```python
from astropulse._generated.models.scan_findings_severity_counts import ScanFindingsSeverityCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ScanFindingsSeverityCounts from a JSON string
scan_findings_severity_counts_instance = ScanFindingsSeverityCounts.from_json(json)
# print the JSON string representation of the object
print(ScanFindingsSeverityCounts.to_json())

# convert the object into a dict
scan_findings_severity_counts_dict = scan_findings_severity_counts_instance.to_dict()
# create an instance of ScanFindingsSeverityCounts from a dict
scan_findings_severity_counts_from_dict = ScanFindingsSeverityCounts.from_dict(scan_findings_severity_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


