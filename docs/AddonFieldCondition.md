# AddonFieldCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The other setting&#39;s dotted path within the add-on&#39;s configuration. | [optional] 
**values** | **List[str]** | What it holds, written as in the configuration: &#x60;true&#x60; for a switch that is on, and an empty string for a setting left out with no &#x60;default&#x60;. A setting left out holds its &#x60;default&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.addon_field_condition import AddonFieldCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AddonFieldCondition from a JSON string
addon_field_condition_instance = AddonFieldCondition.from_json(json)
# print the JSON string representation of the object
print(AddonFieldCondition.to_json())

# convert the object into a dict
addon_field_condition_dict = addon_field_condition_instance.to_dict()
# create an instance of AddonFieldCondition from a dict
addon_field_condition_from_dict = AddonFieldCondition.from_dict(addon_field_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


