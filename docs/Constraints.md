# Constraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**AvailabilityTier**](AvailabilityTier.md) |  | [optional] 
**network_traffic** | [**NetworkTraffic**](NetworkTraffic.md) |  | [optional] 
**resources** | [**AppResource**](AppResource.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.constraints import Constraints

# TODO update the JSON string below
json = "{}"
# create an instance of Constraints from a JSON string
constraints_instance = Constraints.from_json(json)
# print the JSON string representation of the object
print(Constraints.to_json())

# convert the object into a dict
constraints_dict = constraints_instance.to_dict()
# create an instance of Constraints from a dict
constraints_from_dict = Constraints.from_dict(constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


