# ClusterAddonCostSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** |  | [optional] 
**group_by** | [**CostAllocationGroupBy**](CostAllocationGroupBy.md) |  | [optional] 
**interval** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**points** | [**List[CostSeriesPoint]**](CostSeriesPoint.md) |  | [optional] 
**pricing_notes** | [**List[Notice]**](Notice.md) | Say how the cluster&#39;s cost is priced where its figures are not what they seem. | [optional] 
**window** | [**CostWindow**](CostWindow.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_cost_series import ClusterAddonCostSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonCostSeries from a JSON string
cluster_addon_cost_series_instance = ClusterAddonCostSeries.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonCostSeries.to_json())

# convert the object into a dict
cluster_addon_cost_series_dict = cluster_addon_cost_series_instance.to_dict()
# create an instance of ClusterAddonCostSeries from a dict
cluster_addon_cost_series_from_dict = ClusterAddonCostSeries.from_dict(cluster_addon_cost_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


