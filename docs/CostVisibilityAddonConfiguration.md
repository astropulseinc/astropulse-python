# CostVisibilityAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_interval_minutes** | **int** | How often, in minutes, usage is collected, from 1 to 1440; costs are still reported by the hour. | [optional] [default to 5]
**metrics_source** | [**CostMetricsSource**](CostMetricsSource.md) | Where cost reporting reads usage. Left out, it is &#x60;Existing&#x60; when &#x60;prometheusEndpoint&#x60; is set and &#x60;Managed&#x60; otherwise. | [optional] 
**price_sheet** | [**CostPriceSheet**](CostPriceSheet.md) | Your own unit prices, used instead of published ones. Usage with no price is reported as unpriced, never as free. | [optional] 
**pricing** | [**CostPricing**](CostPricing.md) | How usage is priced. Left out, it is &#x60;PriceSheet&#x60; when &#x60;priceSheet&#x60; is set and &#x60;Published&#x60; otherwise. | [optional] 
**pricing_role_arn** | **str** | An AWS IAM role allowed &#x60;ec2:DescribeSpotPriceHistory&#x60;, so Spot nodes are priced at their Spot price on a cluster AstroPulse didn&#39;t create. | [optional] 
**prometheus** | [**CostVisibilityPrometheusConfiguration**](CostVisibilityPrometheusConfiguration.md) | Settings for the Prometheus AstroPulse installs and runs; not accepted with &#x60;prometheusEndpoint&#x60;. | [optional] 
**prometheus_endpoint** | **str** | The address of a Prometheus you already run, reachable from the cluster, to read usage from instead of installing one. | [optional] 

## Example

```python
from astropulse._generated.models.cost_visibility_addon_configuration import CostVisibilityAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CostVisibilityAddonConfiguration from a JSON string
cost_visibility_addon_configuration_instance = CostVisibilityAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(CostVisibilityAddonConfiguration.to_json())

# convert the object into a dict
cost_visibility_addon_configuration_dict = cost_visibility_addon_configuration_instance.to_dict()
# create an instance of CostVisibilityAddonConfiguration from a dict
cost_visibility_addon_configuration_from_dict = CostVisibilityAddonConfiguration.from_dict(cost_visibility_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


