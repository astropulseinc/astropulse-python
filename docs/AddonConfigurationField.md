# AddonConfigurationField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced** | **bool** | Marks a setting most users leave at its default; clients show it in an advanced section. | [optional] 
**default** | **str** | The value a new add-on gets when the setting is left out, written as it is in the configuration. In a cluster&#39;s catalog it is the value that cluster uses; empty when there is none. | [optional] 
**description** | **str** | Says what the setting does, from the field&#39;s own contract. | [optional] 
**enum** | **List[str]** | The complete set of values the setting accepts, empty for a setting that accepts any value of its type. For an array it is what one element accepts. Published so a client offers the choice instead of a free-text box the API then refuses, and so the list cannot drift from the one validation reads. | [optional] 
**enum_schema** | **str** | Names the schema in this API&#39;s document that lists the setting&#39;s values with each one&#39;s display name and meaning, such as &#x60;InstanceType&#x60;. | [optional] 
**format** | [**AddonConfigurationFormat**](AddonConfigurationFormat.md) | The form a text setting&#39;s value takes, empty for text of any form. For an array it is the form of one element. | [optional] 
**label** | **str** | This field&#39;s name for display, such as CPU for resources.cpu. | [optional] 
**leaf** | **bool** | True for a field that takes a value and false for the objects that only give structure: render leaves as inputs and the rest as headings. | [optional] 
**max_items** | **int** | The most entries a list setting accepts, absent when it has no limit. | [optional] 
**maximum** | **float** | The largest value a number setting accepts, absent when it has no upper bound. | [optional] 
**minimum** | **float** | The smallest value a number setting accepts, absent when it has no lower bound. | [optional] 
**path** | **str** | The setting&#39;s dotted path within the add-on&#39;s configuration. | [optional] 
**placeholder** | **str** | A hint for an empty field: an example value such as 250m, or false, 0, [] or {} for its type, and empty for text with no example. | [optional] 
**read_only** | **bool** | Shown for reference; clients don&#39;t offer to change it. | [optional] 
**required** | **bool** | Marks a setting the add-on refuses a configuration without, wherever the setting applies (visibleWhen). | [optional] 
**section** | **str** | The heading this field belongs under, empty for a top-level one. It is the parent object&#39;s label, not its path. | [optional] 
**suggested** | **str** | A value AstroPulse knows would work on this cluster, empty when it knows of none. It is never applied for you. | [optional] 
**suggested_from** | **str** | Says where the suggestion came from, so it reads as a proposal with a reason rather than a value that appeared. | [optional] 
**type** | [**AddonFieldType**](AddonFieldType.md) | The kind of value the setting takes. | [optional] 
**unavailable** | [**List[AddonUnavailableValue]**](AddonUnavailableValue.md) | Values in enum this cluster does not offer, each with why; absent when it offers every one. | [optional] 
**visible_when** | [**AddonFieldCondition**](AddonFieldCondition.md) | When the setting applies: while the other setting it names, itself applying, holds one of &#x60;values&#x60;. A client shows the setting only then; absent when it always applies. | [optional] 

## Example

```python
from astropulse._generated.models.addon_configuration_field import AddonConfigurationField

# TODO update the JSON string below
json = "{}"
# create an instance of AddonConfigurationField from a JSON string
addon_configuration_field_instance = AddonConfigurationField.from_json(json)
# print the JSON string representation of the object
print(AddonConfigurationField.to_json())

# convert the object into a dict
addon_configuration_field_dict = addon_configuration_field_instance.to_dict()
# create an instance of AddonConfigurationField from a dict
addon_configuration_field_from_dict = AddonConfigurationField.from_dict(addon_configuration_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


