# DeploymentDiffItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **object** | The sanitized new value (omitted/redacted for secrets). | [optional] 
**before** | **object** | The sanitized prior value (omitted/redacted for secrets). | [optional] 
**description** | **str** | An optional human explanation of the change. | [optional] 
**path** | **str** | The changed field&#39;s path in the application request, as this API&#39;s document names it, such as &#x60;source.helm.repo.chartVersion&#x60;. Below &#x60;values.object&#x60; it continues with the chart&#39;s own value keys. | [optional] 
**redacted** | **bool** | Indicates the value was hidden: before and after are left out. The text ***REDACTED*** stands for a hidden value and is never accepted as a value when applying. | [optional] 
**secret** | **bool** | Indicates the field is classified as secret-bearing. | [optional] 

## Example

```python
from astropulse._generated.models.deployment_diff_item import DeploymentDiffItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentDiffItem from a JSON string
deployment_diff_item_instance = DeploymentDiffItem.from_json(json)
# print the JSON string representation of the object
print(DeploymentDiffItem.to_json())

# convert the object into a dict
deployment_diff_item_dict = deployment_diff_item_instance.to_dict()
# create an instance of DeploymentDiffItem from a dict
deployment_diff_item_from_dict = DeploymentDiffItem.from_dict(deployment_diff_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


