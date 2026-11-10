# ClusterCostSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**group_by** | [**CostAllocationGroupBy**](CostAllocationGroupBy.md) | The breakdown &#x60;name&#x60; is a row of; absent for the whole cluster. | [optional] 
**interval** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**points** | [**List[CostSeriesPoint]**](CostSeriesPoint.md) |  | [optional] 
**pricing_notes** | [**List[Notice]**](Notice.md) | Say how the cluster&#39;s cost is priced where its figures are not what they seem. | [optional] 
**window** | [**CostWindow**](CostWindow.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_cost_series import ClusterCostSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCostSeries from a JSON string
cluster_cost_series_instance = ClusterCostSeries.from_json(json)
# print the JSON string representation of the object
print(ClusterCostSeries.to_json())

# convert the object into a dict
cluster_cost_series_dict = cluster_cost_series_instance.to_dict()
# create an instance of ClusterCostSeries from a dict
cluster_cost_series_from_dict = ClusterCostSeries.from_dict(cluster_cost_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


