# ClusterCostSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**complete** | **bool** |  | [optional] 
**costs** | [**List[CostTotal]**](CostTotal.md) |  | [optional] 
**coverage_percent** | **float** | MeasuredWindows divided by ExpectedWindows. | [optional] 
**dimensions** | [**CostDimensions**](CostDimensions.md) |  | [optional] 
**empty_message** | **str** | Says why the window has no cost and what to do next. Set only when no hour in the window was measured. | [optional] 
**expected_windows** | **int** |  | [optional] 
**gap_windows** | **int** |  | [optional] 
**last_received_at** | **str** |  | [optional] 
**measured_windows** | **int** | Excludes both missing reports and explicit gaps. | [optional] 
**missing_windows** | **int** |  | [optional] 
**priced_from** | **str** | The start of the first measured hour that carries a price. Absent when no hour is priced. | [optional] 
**priced_windows** | **int** | The number of measured hours that carry a price. | [optional] 
**pricing_notes** | [**List[Notice]**](Notice.md) | Say how the cluster&#39;s cost is priced where its figures are not what they seem. | [optional] 
**reported_windows** | **int** |  | [optional] 
**unpriced_windows** | **int** | The number of measured hours with no price: their usage is in the dimensions and not in the costs. | [optional] 
**window** | [**CostWindow**](CostWindow.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_cost_summary import ClusterCostSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCostSummary from a JSON string
cluster_cost_summary_instance = ClusterCostSummary.from_json(json)
# print the JSON string representation of the object
print(ClusterCostSummary.to_json())

# convert the object into a dict
cluster_cost_summary_dict = cluster_cost_summary_instance.to_dict()
# create an instance of ClusterCostSummary from a dict
cluster_cost_summary_from_dict = ClusterCostSummary.from_dict(cluster_cost_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


