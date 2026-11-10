# ScanFindingOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**ScanFindingOwnerType**](ScanFindingOwnerType.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.scan_finding_owner import ScanFindingOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ScanFindingOwner from a JSON string
scan_finding_owner_instance = ScanFindingOwner.from_json(json)
# print the JSON string representation of the object
print(ScanFindingOwner.to_json())

# convert the object into a dict
scan_finding_owner_dict = scan_finding_owner_instance.to_dict()
# create an instance of ScanFindingOwner from a dict
scan_finding_owner_from_dict = ScanFindingOwner.from_dict(scan_finding_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


