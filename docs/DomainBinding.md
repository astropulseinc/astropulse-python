# DomainBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | The application the hostname serves. | [optional] 
**created_at** | **datetime** | When the hostname was bound. | [optional] 
**failure_reason** | **str** | Why the binding failed; absent unless it did. | [optional] 
**hostname** | **str** | The bound hostname. | [optional] 
**hostname_source** | [**DomainHostnameSource**](DomainHostnameSource.md) | Where the hostname came from. | [optional] 
**status** | [**DomainBindingStatus**](DomainBindingStatus.md) | Whether the hostname serves the application yet. | [optional] 
**updated_at** | **datetime** | When the binding last changed. | [optional] 

## Example

```python
from astropulse._generated.models.domain_binding import DomainBinding

# TODO update the JSON string below
json = "{}"
# create an instance of DomainBinding from a JSON string
domain_binding_instance = DomainBinding.from_json(json)
# print the JSON string representation of the object
print(DomainBinding.to_json())

# convert the object into a dict
domain_binding_dict = domain_binding_instance.to_dict()
# create an instance of DomainBinding from a dict
domain_binding_from_dict = DomainBinding.from_dict(domain_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


