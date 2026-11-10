# ImageScanFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_count** | **int** | How many containers in this workload run this image. Blast radius, never a multiplier on Counts. | [optional] 
**counts** | [**ScanFindingsSeverityCounts**](ScanFindingsSeverityCounts.md) | The distinct findings in this image, deduplicated by vulnerability, package, and installed version. | [optional] 
**fixable** | **int** | How many of Counts have a published fixed version — the difference between \&quot;bump the tag\&quot; and \&quot;accept or replace\&quot;. | [optional] 
**image** | **str** | The repository and tag or digest to update when remediating a finding. | [optional] 

## Example

```python
from astropulse._generated.models.image_scan_finding import ImageScanFinding

# TODO update the JSON string below
json = "{}"
# create an instance of ImageScanFinding from a JSON string
image_scan_finding_instance = ImageScanFinding.from_json(json)
# print the JSON string representation of the object
print(ImageScanFinding.to_json())

# convert the object into a dict
image_scan_finding_dict = image_scan_finding_instance.to_dict()
# create an instance of ImageScanFinding from a dict
image_scan_finding_from_dict = ImageScanFinding.from_dict(image_scan_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


