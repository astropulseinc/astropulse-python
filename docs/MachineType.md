# MachineType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerators** | [**List[Accelerator]**](Accelerator.md) |  | [optional] 
**architecture** | **List[str]** |  | [optional] 
**category** | **str** |  | [optional] 
**infos** | **Dict[str, object]** |  | [optional] 
**memory_mb** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**on_demand_price_per_hour** | **str** |  | [optional] 
**os_platform** | **str** |  | [optional] 
**spot_price_per_hour** | **str** |  | [optional] 
**time_generated** | **str** |  | [optional] 
**v_cpu** | **int** |  | [optional] 
**zone** | **str** |  | [optional] 
**zones** | **List[str]** | Lists every zone in the region offering this machine. Populated by the region-wide (zone \&quot;all\&quot;) view; availability differs between zones, so per-zone placement must never be assumed from a single zone. | [optional] 

## Example

```python
from astropulse._generated.models.machine_type import MachineType

# TODO update the JSON string below
json = "{}"
# create an instance of MachineType from a JSON string
machine_type_instance = MachineType.from_json(json)
# print the JSON string representation of the object
print(MachineType.to_json())

# convert the object into a dict
machine_type_dict = machine_type_instance.to_dict()
# create an instance of MachineType from a dict
machine_type_from_dict = MachineType.from_dict(machine_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


