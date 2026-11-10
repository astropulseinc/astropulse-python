# ClusterCostSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterCostSummary**](ClusterCostSummary.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_cost_summary_response import ClusterCostSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCostSummaryResponse from a JSON string
cluster_cost_summary_response_instance = ClusterCostSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterCostSummaryResponse.to_json())

# convert the object into a dict
cluster_cost_summary_response_dict = cluster_cost_summary_response_instance.to_dict()
# create an instance of ClusterCostSummaryResponse from a dict
cluster_cost_summary_response_from_dict = ClusterCostSummaryResponse.from_dict(cluster_cost_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


