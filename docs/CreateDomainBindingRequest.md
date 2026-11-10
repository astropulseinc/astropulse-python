# CreateDomainBindingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | 
**hostname** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.create_domain_binding_request import CreateDomainBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainBindingRequest from a JSON string
create_domain_binding_request_instance = CreateDomainBindingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDomainBindingRequest.to_json())

# convert the object into a dict
create_domain_binding_request_dict = create_domain_binding_request_instance.to_dict()
# create an instance of CreateDomainBindingRequest from a dict
create_domain_binding_request_from_dict = CreateDomainBindingRequest.from_dict(create_domain_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


