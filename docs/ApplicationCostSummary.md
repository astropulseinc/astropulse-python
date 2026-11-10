# ApplicationCostSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**complete** | **bool** |  | [optional] 
**costs** | [**List[CostTotal]**](CostTotal.md) |  | [optional] 
**coverage_percent** | **float** |  | [optional] 
**dimensions** | [**CostDimensions**](CostDimensions.md) |  | [optional] 
**expected_windows** | **int** |  | [optional] 
**gap_windows** | **int** |  | [optional] 
**measured_windows** | **int** |  | [optional] 
**missing_windows** | **int** |  | [optional] 
**priced_from** | **str** | The start of the first measured hour that carries a price. Absent when no hour is priced. | [optional] 
**priced_windows** | **int** | The number of measured hours that carry a price. | [optional] 
**pricing_notes** | [**List[Notice]**](Notice.md) | Say how the cluster&#39;s cost is priced where its figures are not what they seem. | [optional] 
**reported_windows** | **int** |  | [optional] 
**reporting** | **bool** |  | [optional] 
**unpriced_windows** | **int** | The number of measured hours with no price: their usage is in the dimensions and not in the costs. | [optional] 
**window** | [**CostWindow**](CostWindow.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.application_cost_summary import ApplicationCostSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCostSummary from a JSON string
application_cost_summary_instance = ApplicationCostSummary.from_json(json)
# print the JSON string representation of the object
print(ApplicationCostSummary.to_json())

# convert the object into a dict
application_cost_summary_dict = application_cost_summary_instance.to_dict()
# create an instance of ApplicationCostSummary from a dict
application_cost_summary_from_dict = ApplicationCostSummary.from_dict(application_cost_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


