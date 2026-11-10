# SubnetSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | The CIDR block of the subnet (optional), for example 10.0.1.0/24. | [optional] 
**id** | **str** | The cloud provider subnet ID (required). | 
**type** | [**SubnetType**](SubnetType.md) | Whether the subnet is public or private. | 

## Example

```python
from astropulse._generated.models.subnet_spec import SubnetSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetSpec from a JSON string
subnet_spec_instance = SubnetSpec.from_json(json)
# print the JSON string representation of the object
print(SubnetSpec.to_json())

# convert the object into a dict
subnet_spec_dict = subnet_spec_instance.to_dict()
# create an instance of SubnetSpec from a dict
subnet_spec_from_dict = SubnetSpec.from_dict(subnet_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


