# DomainBindingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DomainBinding**](DomainBinding.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.domain_binding_response import DomainBindingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainBindingResponse from a JSON string
domain_binding_response_instance = DomainBindingResponse.from_json(json)
# print the JSON string representation of the object
print(DomainBindingResponse.to_json())

# convert the object into a dict
domain_binding_response_dict = domain_binding_response_instance.to_dict()
# create an instance of DomainBindingResponse from a dict
domain_binding_response_from_dict = DomainBindingResponse.from_dict(domain_binding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


