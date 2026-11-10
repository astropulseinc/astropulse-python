# ResourceCapacityCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_utilization** | **str** |  | [optional] 
**current_nodes** | **int** |  | [optional] 
**has_capacity** | **bool** |  | [optional] 
**memory_utilization** | **str** |  | [optional] 
**required_for_surge** | **int** |  | [optional] 

## Example

```python
from astropulse._generated.models.resource_capacity_check import ResourceCapacityCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCapacityCheck from a JSON string
resource_capacity_check_instance = ResourceCapacityCheck.from_json(json)
# print the JSON string representation of the object
print(ResourceCapacityCheck.to_json())

# convert the object into a dict
resource_capacity_check_dict = resource_capacity_check_instance.to_dict()
# create an instance of ResourceCapacityCheck from a dict
resource_capacity_check_from_dict = ResourceCapacityCheck.from_dict(resource_capacity_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


