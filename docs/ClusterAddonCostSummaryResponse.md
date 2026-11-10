# ClusterAddonCostSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAddonCostSummary**](ClusterAddonCostSummary.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_cost_summary_response import ClusterAddonCostSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonCostSummaryResponse from a JSON string
cluster_addon_cost_summary_response_instance = ClusterAddonCostSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonCostSummaryResponse.to_json())

# convert the object into a dict
cluster_addon_cost_summary_response_dict = cluster_addon_cost_summary_response_instance.to_dict()
# create an instance of ClusterAddonCostSummaryResponse from a dict
cluster_addon_cost_summary_response_from_dict = ClusterAddonCostSummaryResponse.from_dict(cluster_addon_cost_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


