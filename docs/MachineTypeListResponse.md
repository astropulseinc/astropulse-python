# MachineTypeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MachineType]**](MachineType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.machine_type_list_response import MachineTypeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MachineTypeListResponse from a JSON string
machine_type_list_response_instance = MachineTypeListResponse.from_json(json)
# print the JSON string representation of the object
print(MachineTypeListResponse.to_json())

# convert the object into a dict
machine_type_list_response_dict = machine_type_list_response_instance.to_dict()
# create an instance of MachineTypeListResponse from a dict
machine_type_list_response_from_dict = MachineTypeListResponse.from_dict(machine_type_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


