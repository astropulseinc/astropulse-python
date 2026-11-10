# ScanFindingsUnscannedImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | How many images could not be scanned for this reason; 0 when not known. | [optional] 
**images** | **List[str]** | Names up to three of them; Count includes the rest. | [optional] 
**notice** | [**Notice**](Notice.md) | Says why these images have no findings and what to do; its code is &#x60;ScanRegistryDenied&#x60;, &#x60;ScanTimedOut&#x60;, &#x60;ScanResultNotStored&#x60; or &#x60;ScanNoteUnreadable&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.scan_findings_unscanned_images import ScanFindingsUnscannedImages

# TODO update the JSON string below
json = "{}"
# create an instance of ScanFindingsUnscannedImages from a JSON string
scan_findings_unscanned_images_instance = ScanFindingsUnscannedImages.from_json(json)
# print the JSON string representation of the object
print(ScanFindingsUnscannedImages.to_json())

# convert the object into a dict
scan_findings_unscanned_images_dict = scan_findings_unscanned_images_instance.to_dict()
# create an instance of ScanFindingsUnscannedImages from a dict
scan_findings_unscanned_images_from_dict = ScanFindingsUnscannedImages.from_dict(scan_findings_unscanned_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


