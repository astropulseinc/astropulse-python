# NginxAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | Added to the controller&#39;s Service, for cloud load-balancer settings the provider reads from there. | [optional] 
**auto_scaling** | [**AddonAutoScalingConfig**](AddonAutoScalingConfig.md) | Scales the controller itself with load. | [optional] 
**default_tls_mode** | [**TLSMode**](TLSMode.md) | The TLS mode an application gets when it names none: Wildcard or Certificate. Empty takes Wildcard when the wildcard certificate is on, Certificate otherwise. | [optional] 
**enable_node_port** | **bool** | Publishes the controller on a NodePort instead of a cloud load balancer, for clusters that have none. | [optional] 
**exposure** | [**EndpointExposure**](EndpointExposure.md) | Who can reach the controller&#39;s load balancer, and so every Ingress it serves: Public (the internet, the default) or Private (only the cluster&#39;s network). | [optional] 
**ingress_class_name** | **str** | The class this controller answers to. Empty takes the AstroPulse default. | [optional] [default to 'nginx']
**node_selector** | **str** | Confines the controller to matching nodes, as key&#x3D;value. | [optional] 
**replicas** | **int** | How many controller pods to run. Empty takes the AstroPulse default. | [optional] 
**ssl_passthrough** | **bool** | Lets applications that serve their own TLS receive it still encrypted: an image application using TLS mode &#x60;Passthrough&#x60;, or an Ingress of your own annotated nginx.ingress.kubernetes.io/ssl-passthrough. Every other application&#39;s TLS is terminated at the controller. | [optional] 
**wildcard_certificate** | [**NginxWildcardCertificate**](NginxWildcardCertificate.md) | One certificate for a domain and every name one level below it, served to applications using TLS mode &#x60;Wildcard&#x60;. | [optional] 

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


