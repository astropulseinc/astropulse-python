# ExternalDNSAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_access** | [**CloudAccessMode**](CloudAccessMode.md) | How external-dns signs in to your DNS provider. Left out, it is &#x60;Identity&#x60; when &#x60;identity&#x60; is set, &#x60;Secret&#x60; when &#x60;secretRef&#x60; is set, and &#x60;None&#x60; otherwise. | [optional] 
**domain_filter** | **str** | The DNS zones external-dns may change, such as example.com, separated by commas. Left out, it is your organization&#39;s verified domains when it runs as the identity AstroPulse created (refused if you have none), and otherwise every zone its credentials reach. | [optional] 
**dry_run** | **bool** | Logs the DNS changes external-dns would make without making them. | [optional] 
**gateway_routes** | **bool** | Also publishes DNS for the hostnames of Gateway API routes, not only Ingress hostnames; needs the Gateway API on the cluster. | [optional] 
**identity** | [**AddonWorkloadIdentity**](AddonWorkloadIdentity.md) | The cloud identity external-dns runs as to change records in your DNS zone. On an EKS cluster AstroPulse created it defaults to the role made for it; on a registered cluster using Route 53, set this or &#x60;secretRef&#x60;. | [optional] 
**policy** | [**ExternalDNSPolicy**](ExternalDNSPolicy.md) | What external-dns may do to the records it owns. Left out, an update keeps the current value and a new add-on uses &#x60;Sync&#x60;. | [optional] 
**provider** | [**ExternalDNSProvider**](ExternalDNSProvider.md) | The DNS service that holds your zone. Left out, it is the cluster&#39;s own cloud, and refused when that is not known. | [optional] 
**secret_ref** | **str** | The name of a Secret in the add-on&#39;s namespace holding DNS provider credentials. Use it only where a cloud identity can&#39;t be used, such as a zone in another cloud; it can&#39;t be combined with &#x60;identity&#x60;. | [optional] 
**txt_owner_id** | **str** | The owner name written on this cluster&#39;s DNS records, so clusters sharing a zone leave each other&#39;s records alone. Left out, it keeps the current value, or on a first install is made from the cluster&#39;s name. | [optional] 

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


