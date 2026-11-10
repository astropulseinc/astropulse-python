# ClusterAddonCostSeriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAddonCostSeries**](ClusterAddonCostSeries.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_cost_series_response import ClusterAddonCostSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonCostSeriesResponse from a JSON string
cluster_addon_cost_series_response_instance = ClusterAddonCostSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonCostSeriesResponse.to_json())

# convert the object into a dict
cluster_addon_cost_series_response_dict = cluster_addon_cost_series_response_instance.to_dict()
# create an instance of ClusterAddonCostSeriesResponse from a dict
cluster_addon_cost_series_response_from_dict = ClusterAddonCostSeriesResponse.from_dict(cluster_addon_cost_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


