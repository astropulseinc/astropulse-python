# GatewayAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scaling** | [**GatewayAutoScalingConfig**](GatewayAutoScalingConfig.md) | Adds and removes gateway proxy copies as load changes. Left out or off, one copy runs. | [optional] 
**enable_node_port** | **bool** | Serves the gateway on a port of every node instead of a cloud load balancer; turn it on for a cluster that cannot create one. | [optional] 
**exposure** | [**EndpointExposure**](EndpointExposure.md) | Who can reach the shared gateway, and the default for model endpoints that name none. | [optional] 

## Example

```python
from astropulse._generated.models.gateway_addon_configuration import GatewayAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayAddonConfiguration from a JSON string
gateway_addon_configuration_instance = GatewayAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(GatewayAddonConfiguration.to_json())

# convert the object into a dict
gateway_addon_configuration_dict = gateway_addon_configuration_instance.to_dict()
# create an instance of GatewayAddonConfiguration from a dict
gateway_addon_configuration_from_dict = GatewayAddonConfiguration.from_dict(gateway_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


