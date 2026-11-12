# GatewayAutoScalingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Turns automatic scaling of the gateway proxy on. | [optional] 
**max_replicas** | **int** | The most copies that may run. Left out, it is 10. | [optional] [default to 10]
**metric** | [**GatewayScalingMetric**](GatewayScalingMetric.md) | What scaling follows. Left out, it is &#x60;CPU&#x60;. | [optional] 
**min_replicas** | **int** | The fewest copies that keep running. Left out, it is 2. | [optional] [default to 2]
**target_cpu_percent** | **int** | The average CPU use, in percent, that scaling keeps each copy at. Left out, it is 70. | [optional] [default to 70]
**target_requests_per_second** | **int** | The requests per second each copy handles before another is added. Left out, it is 500. | [optional] [default to 500]

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


