# GatewayAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scaling** | [**GatewayAutoScalingConfig**](GatewayAutoScalingConfig.md) | Scales the merged Envoy proxy behind the Gateway. Omitted or disabled keeps one fixed replica. | [optional] 
**enable_node_port** | **bool** | Publishes the gateway on a NodePort instead of a cloud load balancer, for clusters that have none. | [optional] 
**exposure** | [**EndpointExposure**](EndpointExposure.md) | The default for model endpoints that name none, and the exposure of the shared Gateway: Public (the internet, the default) or Private (only the cluster&#39;s network). | [optional] 

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


