# MachineTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MachineType**](MachineType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.machine_type_response import MachineTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTypeResponse from a JSON string
machine_type_response_instance = MachineTypeResponse.from_json(json)
# print the JSON string representation of the object
print(MachineTypeResponse.to_json())

# convert the object into a dict
machine_type_response_dict = machine_type_response_instance.to_dict()
# create an instance of MachineTypeResponse from a dict
machine_type_response_from_dict = MachineTypeResponse.from_dict(machine_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


