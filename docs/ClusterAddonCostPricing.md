# ClusterAddonCostPricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notices** | [**List[Notice]**](Notice.md) | Say what is priced differently and what to do. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_cost_pricing import ClusterAddonCostPricing

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonCostPricing from a JSON string
cluster_addon_cost_pricing_instance = ClusterAddonCostPricing.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonCostPricing.to_json())

# convert the object into a dict
cluster_addon_cost_pricing_dict = cluster_addon_cost_pricing_instance.to_dict()
# create an instance of ClusterAddonCostPricing from a dict
cluster_addon_cost_pricing_from_dict = ClusterAddonCostPricing.from_dict(cluster_addon_cost_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


