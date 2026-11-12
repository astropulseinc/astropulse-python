# NginxAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | Extra annotations on the controller&#39;s load balancer Service, for settings your cloud reads from there. | [optional] 
**auto_scaling** | [**AddonAutoScalingConfig**](AddonAutoScalingConfig.md) | Adds and removes controller copies as load changes. | [optional] 
**default_tls_mode** | [**TLSMode**](TLSMode.md) | The TLS mode of an application that names none. Left out, it is &#x60;Wildcard&#x60; when the wildcard certificate is on and &#x60;Certificate&#x60; otherwise. | [optional] 
**enable_node_port** | **bool** | Serves the controller on a port of every node instead of a cloud load balancer; turn it on for a cluster that cannot create one. | [optional] 
**exposure** | [**EndpointExposure**](EndpointExposure.md) | Who can reach the controller&#39;s load balancer, and so every application it serves. | [optional] 
**ingress_class_name** | **str** | The ingress class applications use to choose this controller. Left out, it is &#x60;nginx&#x60;. | [optional] [default to 'nginx']
**node_selector** | **str** | Runs the controller only on nodes with this label, written key&#x3D;value. | [optional] 
**replicas** | **int** | How many copies of the controller run. Left out, AstroPulse&#39;s default applies. | [optional] 
**ssl_passthrough** | **bool** | Passes HTTPS through, still encrypted, to applications that serve their own certificate: an application with TLS mode &#x60;Passthrough&#x60;, or your own Ingress annotated &#x60;nginx.ingress.kubernetes.io/ssl-passthrough&#x60;. Every other application&#39;s HTTPS is decrypted at the controller. | [optional] 
**wildcard_certificate** | [**NginxWildcardCertificate**](NginxWildcardCertificate.md) | One certificate for a domain and every name directly under it, served to applications with TLS mode &#x60;Wildcard&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.nginx_addon_configuration import NginxAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of NginxAddonConfiguration from a JSON string
nginx_addon_configuration_instance = NginxAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(NginxAddonConfiguration.to_json())

# convert the object into a dict
nginx_addon_configuration_dict = nginx_addon_configuration_instance.to_dict()
# create an instance of NginxAddonConfiguration from a dict
nginx_addon_configuration_from_dict = NginxAddonConfiguration.from_dict(nginx_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


