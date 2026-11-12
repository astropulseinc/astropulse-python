# KarpenterCapacityReservations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | Capacity reservation IDs, such as cr-0123456789abcdef0, listed in the EC2 console under Capacity Reservations. | [optional] 
**tags** | **List[str]** | The tags, written key&#x3D;value, that a reservation must all carry; unlike an ID, a tag keeps matching a renewed reservation. | [optional] 

## Example

```python
from astropulse._generated.models.karpenter_capacity_reservations import KarpenterCapacityReservations

# TODO update the JSON string below
json = "{}"
# create an instance of KarpenterCapacityReservations from a JSON string
karpenter_capacity_reservations_instance = KarpenterCapacityReservations.from_json(json)
# print the JSON string representation of the object
print(KarpenterCapacityReservations.to_json())

# convert the object into a dict
karpenter_capacity_reservations_dict = karpenter_capacity_reservations_instance.to_dict()
# create an instance of KarpenterCapacityReservations from a dict
karpenter_capacity_reservations_from_dict = KarpenterCapacityReservations.from_dict(karpenter_capacity_reservations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


