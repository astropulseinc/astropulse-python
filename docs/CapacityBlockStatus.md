# CapacityBlockStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** | The zone the block reserves capacity in. | [optional] 
**end_time** | **str** | When the block ends, RFC 3339. The group&#39;s nodes are terminated when the block ends. | [optional] 
**instance_count** | **int** | How many instances the block reserves. | [optional] 
**instance_type** | **str** | The instance type the block reserves. | [optional] 
**phase** | [**CapacityBlockPhase**](CapacityBlockPhase.md) | Where the block stands now. An ended block&#39;s node group runs no nodes; delete it, or create a new CapacityBlock node group on a new block. | [optional] 
**reservation_id** | **str** | The block&#39;s capacity reservation id. | [optional] 
**start_time** | **str** | When the block starts, RFC 3339. | [optional] 

## Example

```python
from astropulse._generated.models.capacity_block_status import CapacityBlockStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityBlockStatus from a JSON string
capacity_block_status_instance = CapacityBlockStatus.from_json(json)
# print the JSON string representation of the object
print(CapacityBlockStatus.to_json())

# convert the object into a dict
capacity_block_status_dict = capacity_block_status_instance.to_dict()
# create an instance of CapacityBlockStatus from a dict
capacity_block_status_from_dict = CapacityBlockStatus.from_dict(capacity_block_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


