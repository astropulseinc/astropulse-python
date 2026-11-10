# CostVisibilityPrometheusConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | **str** | The local raw-metric recovery window. It accepts whole hours or days from 24h through 7d; empty selects the Astro default of 7d. | [optional] [default to '7d']
**storage** | [**CostVisibilityPrometheusStorageConfiguration**](CostVisibilityPrometheusStorageConfiguration.md) | Configures the Prometheus data volume. Empty selects an Astro-sized volume on the cluster&#39;s default storage. | [optional] 

## Example

```python
from astropulse._generated.models.cost_visibility_prometheus_configuration import CostVisibilityPrometheusConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CostVisibilityPrometheusConfiguration from a JSON string
cost_visibility_prometheus_configuration_instance = CostVisibilityPrometheusConfiguration.from_json(json)
# print the JSON string representation of the object
print(CostVisibilityPrometheusConfiguration.to_json())

# convert the object into a dict
cost_visibility_prometheus_configuration_dict = cost_visibility_prometheus_configuration_instance.to_dict()
# create an instance of CostVisibilityPrometheusConfiguration from a dict
cost_visibility_prometheus_configuration_from_dict = CostVisibilityPrometheusConfiguration.from_dict(cost_visibility_prometheus_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


