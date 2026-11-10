# GatewayAutoScalingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Turns horizontal autoscaling on for the proxy. | [optional] 
**max_replicas** | **int** | The replica ceiling. Empty takes the AstroPulse default (10). | [optional] [default to 10]
**metric** | [**GatewayScalingMetric**](GatewayScalingMetric.md) | The one signal replicas follow. Empty means CPU. | [optional] 
**min_replicas** | **int** | The replica floor. Empty takes the AstroPulse default (2). | [optional] [default to 2]
**target_cpu_percent** | **int** | The CPU utilisation to hold under metric CPU. Empty takes the AstroPulse default (70). | [optional] [default to 70]
**target_requests_per_second** | **int** | The per-replica request rate to hold under metric RequestsPerSecond. Empty takes the AstroPulse default (500). | [optional] [default to 500]

## Example

```python
from astropulse._generated.models.gateway_auto_scaling_config import GatewayAutoScalingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayAutoScalingConfig from a JSON string
gateway_auto_scaling_config_instance = GatewayAutoScalingConfig.from_json(json)
# print the JSON string representation of the object
print(GatewayAutoScalingConfig.to_json())

# convert the object into a dict
gateway_auto_scaling_config_dict = gateway_auto_scaling_config_instance.to_dict()
# create an instance of GatewayAutoScalingConfig from a dict
gateway_auto_scaling_config_from_dict = GatewayAutoScalingConfig.from_dict(gateway_auto_scaling_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


