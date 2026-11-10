# CapacityReservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_count** | **int** | How many instances are free now. | [optional] 
**end_date** | **str** | When the reservation ends, when it has one. | [optional] 
**gpu_pool_reason** | **str** | Says why the GPU pool could not, when it cannot. | [optional] 
**gpu_pool_usable** | **bool** | True when the Karpenter GPU pool could launch into it. | [optional] 
**id** | **str** | The reservation ID. | [optional] 
**kind** | [**CapacityReservationKind**](CapacityReservationKind.md) | Whether the capacity is an On-Demand Capacity Reservation or a Capacity Block for ML. | [optional] 
**machine_type** | **str** | The instance type reserved. | [optional] 
**node_group_instance_type** | [**InstanceType**](InstanceType.md) | The instanceType a node group sets to run on it. | [optional] 
**node_group_reason** | **str** | Says why no node group could, when one cannot. | [optional] 
**node_group_usable** | **bool** | True when a node group in the cluster&#39;s zones could run on it. | [optional] 
**start_date** | **str** | When the reservation starts, when it has one. | [optional] 
**state** | **str** | The cloud&#39;s state for the reservation (active, scheduled, ...). | [optional] 
**total_count** | **int** | How many instances are reserved. | [optional] 
**zone** | **str** | The availability zone. | [optional] 

## Example

```python
from astropulse._generated.models.capacity_reservation import CapacityReservation

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityReservation from a JSON string
capacity_reservation_instance = CapacityReservation.from_json(json)
# print the JSON string representation of the object
print(CapacityReservation.to_json())

# convert the object into a dict
capacity_reservation_dict = capacity_reservation_instance.to_dict()
# create an instance of CapacityReservation from a dict
capacity_reservation_from_dict = CapacityReservation.from_dict(capacity_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


