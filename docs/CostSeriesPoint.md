# CostSeriesPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** |  | [optional] 
**costs** | [**List[CostTotal]**](CostTotal.md) |  | [optional] 
**coverage_percent** | **float** | MeasuredWindows divided by ExpectedWindows. | [optional] 
**dimensions** | [**CostDimensions**](CostDimensions.md) |  | [optional] 
**expected_windows** | **int** |  | [optional] 
**gap_windows** | **int** |  | [optional] 
**measured_windows** | **int** | Excludes both missing reports and explicit gaps. | [optional] 
**missing_windows** | **int** |  | [optional] 
**reported_windows** | **int** |  | [optional] 
**window** | [**CostWindow**](CostWindow.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.cost_series_point import CostSeriesPoint

# TODO update the JSON string below
json = "{}"
# create an instance of CostSeriesPoint from a JSON string
cost_series_point_instance = CostSeriesPoint.from_json(json)
# print the JSON string representation of the object
print(CostSeriesPoint.to_json())

# convert the object into a dict
cost_series_point_dict = cost_series_point_instance.to_dict()
# create an instance of CostSeriesPoint from a dict
cost_series_point_from_dict = CostSeriesPoint.from_dict(cost_series_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


