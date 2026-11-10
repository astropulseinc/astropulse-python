# CapacityReservationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CapacityReservation]**](CapacityReservation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.capacity_reservation_list_response import CapacityReservationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityReservationListResponse from a JSON string
capacity_reservation_list_response_instance = CapacityReservationListResponse.from_json(json)
# print the JSON string representation of the object
print(CapacityReservationListResponse.to_json())

# convert the object into a dict
capacity_reservation_list_response_dict = capacity_reservation_list_response_instance.to_dict()
# create an instance of CapacityReservationListResponse from a dict
capacity_reservation_list_response_from_dict = CapacityReservationListResponse.from_dict(capacity_reservation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


