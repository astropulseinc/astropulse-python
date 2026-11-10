# ClusterMetricsAllocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterMetricsAllocation**](ClusterMetricsAllocation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_metrics_allocation_response import ClusterMetricsAllocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetricsAllocationResponse from a JSON string
cluster_metrics_allocation_response_instance = ClusterMetricsAllocationResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterMetricsAllocationResponse.to_json())

# convert the object into a dict
cluster_metrics_allocation_response_dict = cluster_metrics_allocation_response_instance.to_dict()
# create an instance of ClusterMetricsAllocationResponse from a dict
cluster_metrics_allocation_response_from_dict = ClusterMetricsAllocationResponse.from_dict(cluster_metrics_allocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


