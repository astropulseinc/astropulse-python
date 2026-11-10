# ClusterCostAllocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterCostAllocation**](ClusterCostAllocation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_cost_allocation_response import ClusterCostAllocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCostAllocationResponse from a JSON string
cluster_cost_allocation_response_instance = ClusterCostAllocationResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterCostAllocationResponse.to_json())

# convert the object into a dict
cluster_cost_allocation_response_dict = cluster_cost_allocation_response_instance.to_dict()
# create an instance of ClusterCostAllocationResponse from a dict
cluster_cost_allocation_response_from_dict = ClusterCostAllocationResponse.from_dict(cluster_cost_allocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


