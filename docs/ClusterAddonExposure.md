# ClusterAddonExposure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The load balancer IPs or hostnames (for the gateway, the addresses its implementation published). Empty on NodePort and until the cloud provisions the balancer. | [optional] 
**message** | **str** | Explains an empty or partial exposure (balancer still being provisioned, agent not connected, the Gateway&#39;s own condition message). | [optional] 
**node_addresses** | [**List[ClusterAddonNodeAddress]**](ClusterAddonNodeAddress.md) | A few node addresses to dial a NodePort on; only set when Type is NodePort. | [optional] 
**note** | **str** | Says what is not open yet and when it opens, for example that HTTPS (443) opens when the first model endpoint is exposed through the gateway. | [optional] 
**ports** | **Dict[str, int]** | Maps a port role (http, https) to the port to dial: the node port on NodePort, the Service port otherwise. | [optional] 
**programmed** | **str** | The Gateway&#39;s Programmed condition (True, False, Unknown); gateway only. | [optional] 
**programmed_state** | [**GatewayProgrammedState**](GatewayProgrammedState.md) | Whether the gateway is ready for traffic, read from programmed; Unknown while it has not said. Gateway only. | [optional] 
**type** | **str** | The exposing Service&#39;s type: LoadBalancer, NodePort or ClusterIP. Empty until the Service has been observed. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_exposure import ClusterAddonExposure

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonExposure from a JSON string
cluster_addon_exposure_instance = ClusterAddonExposure.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonExposure.to_json())

# convert the object into a dict
cluster_addon_exposure_dict = cluster_addon_exposure_instance.to_dict()
# create an instance of ClusterAddonExposure from a dict
cluster_addon_exposure_from_dict = ClusterAddonExposure.from_dict(cluster_addon_exposure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


