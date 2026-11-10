# ScanFindingsNoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | A few words for a table cell or a badge. | [optional] 
**message** | **str** | One or two sentences saying why there is no result and what to change. | [optional] 
**notice** | [**Notice**](Notice.md) | Set when a result is overdue (&#x60;ScanOverdue&#x60;), with the step that gets it scanned. | [optional] 
**owner** | [**ScanFindingOwner**](ScanFindingOwner.md) | The application or add-on. | [optional] 
**reason** | [**ScanFindingsNoResultReason**](ScanFindingsNoResultReason.md) | Why there is no result. | [optional] 

## Example

```python
from astropulse._generated.models.scan_findings_no_result import ScanFindingsNoResult

# TODO update the JSON string below
json = "{}"
# create an instance of ScanFindingsNoResult from a JSON string
scan_findings_no_result_instance = ScanFindingsNoResult.from_json(json)
# print the JSON string representation of the object
print(ScanFindingsNoResult.to_json())

# convert the object into a dict
scan_findings_no_result_dict = scan_findings_no_result_instance.to_dict()
# create an instance of ScanFindingsNoResult from a dict
scan_findings_no_result_from_dict = ScanFindingsNoResult.from_dict(scan_findings_no_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


