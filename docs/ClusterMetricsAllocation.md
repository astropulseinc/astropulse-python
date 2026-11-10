# ClusterMetricsAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**List[ApplicationMetricsAllocationItem]**](ApplicationMetricsAllocationItem.md) | Page-limited by the request&#39;s limit/offset. Unlike ClusterCostAllocation&#39;s opaque, window-pinning NextPageToken, paging here is plain offset+limit: a metrics read is a live re-query of a small ephemeral store, not an accounting read over an immutable billing window, so there is nothing to pin and reissuing the read for the next page is always current. | [optional] 
**cluster_id** | **str** | Identifies the cluster. | [optional] 
**cluster_name** | **str** | Its name. | [optional] 
**empty_message** | **str** | Says why no application is listed and what to do next. Set only when none reported usage in the window, or none matched the search. | [optional] 
**has_more** | **bool** | Reports whether another page follows. | [optional] 
**returned_items** | **int** | How many of them this page carries. | [optional] 
**sort_by** | [**ClusterMetricsSortField**](ClusterMetricsSortField.md) | The dimension the page is ordered on. | [optional] 
**sort_order** | [**SortOrder**](SortOrder.md) | The direction the page is ordered in. | [optional] 
**total_items** | **int** | How many applications reported in the window. | [optional] 
**window** | [**CostWindow**](CostWindow.md) | The time range these readings cover. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_metrics_allocation import ClusterMetricsAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetricsAllocation from a JSON string
cluster_metrics_allocation_instance = ClusterMetricsAllocation.from_json(json)
# print the JSON string representation of the object
print(ClusterMetricsAllocation.to_json())

# convert the object into a dict
cluster_metrics_allocation_dict = cluster_metrics_allocation_instance.to_dict()
# create an instance of ClusterMetricsAllocation from a dict
cluster_metrics_allocation_from_dict = ClusterMetricsAllocation.from_dict(cluster_metrics_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


