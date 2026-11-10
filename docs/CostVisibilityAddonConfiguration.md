# CostVisibilityAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_interval_minutes** | **int** | Tunes how often the metering capability polls for closed windows (windows themselves are fixed hourly). | [optional] [default to 5]
**metrics_source** | [**CostMetricsSource**](CostMetricsSource.md) | Where cost reporting reads usage. Left out, it is Existing when prometheusEndpoint is set and Managed otherwise; a read returns the one in use. | [optional] 
**price_sheet** | [**CostPriceSheet**](CostPriceSheet.md) | Supplies custom unit rates and takes precedence over default estimates. Usage without an available rate is reported as unpriced, never as zero cost. | [optional] 
**pricing** | [**CostPricing**](CostPricing.md) | How usage is priced. Left out, it is PriceSheet when priceSheet is set and Published otherwise; a read returns the one in use. | [optional] 
**pricing_role_arn** | **str** | An AWS IAM role allowed ec2:DescribeSpotPriceHistory, so Spot nodes are priced at their Spot price on a cluster AstroPulse did not create. A cluster AstroPulse created on EKS has its own. | [optional] 
**prometheus** | [**CostVisibilityPrometheusConfiguration**](CostVisibilityPrometheusConfiguration.md) | Configures the bundled scoped Prometheus. It is only valid when no endpoint override is set. All low-level operational tuning remains platform-managed. | [optional] 
**prometheus_endpoint** | **str** | Uses an existing in-cluster Prometheus as the metrics source. It must be reachable from workloads in the target cluster. | [optional] 

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


