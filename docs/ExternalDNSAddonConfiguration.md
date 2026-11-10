# ExternalDNSAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_access** | [**CloudAccessMode**](CloudAccessMode.md) | How external-dns reaches your DNS provider. Left out, it is Identity when identity is set, Secret when secretRef is set, and None otherwise; a read returns the one in use. | [optional] 
**domain_filter** | **str** | The DNS zone external-dns may write to, such as example.com, comma-separated for several. Empty means your organization&#39;s verified domains when it runs as the identity AstroPulse created, and is refused if you have none; otherwise, every zone its credentials can reach. | [optional] 
**dry_run** | **bool** | Logs what external-dns would publish without publishing it. | [optional] 
**gateway_routes** | **bool** | Also publishes DNS for the hostnames of Gateway API HTTPRoutes, alongside the Ingress hostnames external-dns publishes by default. Requires the Gateway API CRDs on the cluster. | [optional] 
**identity** | [**AddonWorkloadIdentity**](AddonWorkloadIdentity.md) | Binds external-dns to a cloud workload identity that can change records in your DNS zone. Annotations render onto its ServiceAccount, labels onto its pods. On an EKS cluster AstroPulse created it defaults to that cluster&#39;s external-dns role; on a registered cluster publishing to Route 53, set it or SecretRef. | [optional] 
**policy** | [**ExternalDNSPolicy**](ExternalDNSPolicy.md) | What external-dns may do to the records it owns: Sync creates, updates and deletes them, and UpsertOnly never deletes them. Left out, an update keeps the current one and a new add-on runs Sync. | [optional] 
**provider** | [**ExternalDNSProvider**](ExternalDNSProvider.md) | The DNS provider to publish through: &#x60;aws&#x60;, &#x60;gcp&#x60; or &#x60;azure&#x60;. Empty selects the cluster&#39;s own cloud, and is refused on a cluster whose cloud is not known. | [optional] 
**secret_ref** | **str** | Names a Secret in the external-dns namespace holding DNS provider credentials. Use it only where a workload identity cannot be used, such as a zone in another cloud; it cannot be combined with identity. | [optional] 
**txt_owner_id** | **str** | Marks the records this cluster owns, so two clusters sharing a zone do not delete each other&#39;s. Empty keeps the value the add-on already uses on this cluster; a first install takes the cluster&#39;s name followed by a suffix unique to the cluster. | [optional] 

## Example

```python
from astropulse._generated.models.external_dns_addon_configuration import ExternalDNSAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDNSAddonConfiguration from a JSON string
external_dns_addon_configuration_instance = ExternalDNSAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(ExternalDNSAddonConfiguration.to_json())

# convert the object into a dict
external_dns_addon_configuration_dict = external_dns_addon_configuration_instance.to_dict()
# create an instance of ExternalDNSAddonConfiguration from a dict
external_dns_addon_configuration_from_dict = ExternalDNSAddonConfiguration.from_dict(external_dns_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


