# ClusterCostSeriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterCostSeries**](ClusterCostSeries.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_cost_series_response import ClusterCostSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCostSeriesResponse from a JSON string
cluster_cost_series_response_instance = ClusterCostSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterCostSeriesResponse.to_json())

# convert the object into a dict
cluster_cost_series_response_dict = cluster_cost_series_response_instance.to_dict()
# create an instance of ClusterCostSeriesResponse from a dict
cluster_cost_series_response_from_dict = ClusterCostSeriesResponse.from_dict(cluster_cost_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


