# ClusterCostAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**List[CostAllocationItem]**](CostAllocationItem.md) |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**complete** | **bool** |  | [optional] 
**coverage_percent** | **float** | MeasuredWindows divided by ExpectedWindows. | [optional] 
**currency** | **str** |  | [optional] 
**expected_windows** | **int** |  | [optional] 
**gap_windows** | **int** |  | [optional] 
**group_by** | [**CostAllocationGroupBy**](CostAllocationGroupBy.md) | What the allocations are broken down by. | [optional] 
**has_more** | **bool** |  | [optional] 
**measured_windows** | **int** | Excludes both missing reports and explicit gaps. | [optional] 
**missing_windows** | **int** |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**priced_from** | **str** | The start of the first measured hour that carries a price. Absent when no hour is priced. | [optional] 
**priced_windows** | **int** | The number of measured hours that carry a price. | [optional] 
**pricing_notes** | [**List[Notice]**](Notice.md) | Say how the cluster&#39;s cost is priced where its figures are not what they seem. | [optional] 
**reported_windows** | **int** |  | [optional] 
**returned_items** | **int** |  | [optional] 
**sort_by** | [**CostAllocationSortBy**](CostAllocationSortBy.md) | What the allocations are ordered by. | [optional] 
**sort_order** | [**SortOrder**](SortOrder.md) | The direction of the order. | [optional] 
**total_items** | **int** |  | [optional] 
**unattributed** | [**List[CostAllocationItem]**](CostAllocationItem.md) | Spend that belongs to no row of the breakdown, such as idle capacity, cluster management and NAT gateways, each with its &#x60;kind&#x60;. It is the same on every page, and with the allocations of every page of an unfiltered breakdown it adds up to the cluster total. | [optional] 
**unpriced_windows** | **int** | The number of measured hours with no price: their usage is in the dimensions and not in the costs. | [optional] 
**window** | [**CostWindow**](CostWindow.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_cost_allocation import ClusterCostAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCostAllocation from a JSON string
cluster_cost_allocation_instance = ClusterCostAllocation.from_json(json)
# print the JSON string representation of the object
print(ClusterCostAllocation.to_json())

# convert the object into a dict
cluster_cost_allocation_dict = cluster_cost_allocation_instance.to_dict()
# create an instance of ClusterCostAllocation from a dict
cluster_cost_allocation_from_dict = ClusterCostAllocation.from_dict(cluster_cost_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


