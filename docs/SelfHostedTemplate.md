# SelfHostedTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The template itself. | [optional] 
**format** | [**TemplateFormat**](TemplateFormat.md) | The template&#39;s format. | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_template import SelfHostedTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedTemplate from a JSON string
self_hosted_template_instance = SelfHostedTemplate.from_json(json)
# print the JSON string representation of the object
print(SelfHostedTemplate.to_json())

# convert the object into a dict
self_hosted_template_dict = self_hosted_template_instance.to_dict()
# create an instance of SelfHostedTemplate from a dict
self_hosted_template_from_dict = SelfHostedTemplate.from_dict(self_hosted_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


