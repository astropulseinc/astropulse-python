# AuditDetailItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The detail&#39;s key in details. | 
**label** | **str** | What the detail is, in words, such as \&quot;Changed fields\&quot;. | 
**value** | **str** | The detail&#39;s value in words. | 

## Example

```python
from astropulse._generated.models.audit_detail_item import AuditDetailItem

# TODO update the JSON string below
json = "{}"
# create an instance of AuditDetailItem from a JSON string
audit_detail_item_instance = AuditDetailItem.from_json(json)
# print the JSON string representation of the object
print(AuditDetailItem.to_json())

# convert the object into a dict
audit_detail_item_dict = audit_detail_item_instance.to_dict()
# create an instance of AuditDetailItem from a dict
audit_detail_item_from_dict = AuditDetailItem.from_dict(audit_detail_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


