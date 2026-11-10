# ValidationIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**severity** | [**UpgradeRiskLevel**](UpgradeRiskLevel.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.validation_issue import ValidationIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationIssue from a JSON string
validation_issue_instance = ValidationIssue.from_json(json)
# print the JSON string representation of the object
print(ValidationIssue.to_json())

# convert the object into a dict
validation_issue_dict = validation_issue_instance.to_dict()
# create an instance of ValidationIssue from a dict
validation_issue_from_dict = ValidationIssue.from_dict(validation_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


