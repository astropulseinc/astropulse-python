# ClusterAddonIngressTLS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | Where an application using the wildcard is served, with its name in place of the first label; empty when the wildcard is off. | [optional] 
**default_mode** | [**TLSMode**](TLSMode.md) | The TLS mode an application gets when it names none and the mode can serve its hostname: Wildcard or Certificate. | [optional] 
**modes** | [**List[ClusterAddonTLSMode]**](ClusterAddonTLSMode.md) | Lists every TLS mode, whether it is offered and, when it is not, what offers it. | [optional] 
**passthrough** | **bool** | Reports whether an application may serve its own TLS. | [optional] 
**wildcard_domain** | **str** | The domain the wildcard certificate covers; empty when the wildcard is off. | [optional] 
**wildcard_stale** | **str** | Says why the wildcard certificate no longer matches the cert-manager add-on&#39;s issuer, and what to apply; empty when it does. | [optional] 
**wildcard_wait** | **str** | Says why the wildcard certificate has not been issued yet; empty once it is. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_ingress_tls import ClusterAddonIngressTLS

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonIngressTLS from a JSON string
cluster_addon_ingress_tls_instance = ClusterAddonIngressTLS.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonIngressTLS.to_json())

# convert the object into a dict
cluster_addon_ingress_tls_dict = cluster_addon_ingress_tls_instance.to_dict()
# create an instance of ClusterAddonIngressTLS from a dict
cluster_addon_ingress_tls_from_dict = ClusterAddonIngressTLS.from_dict(cluster_addon_ingress_tls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


