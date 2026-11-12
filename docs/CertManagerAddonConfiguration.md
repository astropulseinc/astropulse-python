# CertManagerAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_solver** | [**CertManagerDNSSolver**](CertManagerDNSSolver.md) | Proves domain ownership to Let&#39;s Encrypt through your DNS zone, for applications behind an Ingress or the gateway; without it, Ingress certificates are proven over HTTP. Needs a Let&#39;s Encrypt issuer, and on an EKS cluster AstroPulse created defaults to the cluster&#39;s Route 53 zones. | [optional] 
**email** | **str** | The address Let&#39;s Encrypt registers your account under and sends expiry notices to. Required for the Let&#39;s Encrypt issuers. | [optional] 
**enable_cluster_issuer** | **bool** | Creates AstroPulse&#39;s certificate issuers; turn it off to install cert-manager without issuing anything. | [optional] [default to True]
**identity** | [**AddonWorkloadIdentity**](AddonWorkloadIdentity.md) | The cloud identity cert-manager runs as to answer ownership checks in your DNS zone. Required with &#x60;dnsSolver&#x60;, except on an EKS cluster AstroPulse created, where it defaults to the role made for it. | [optional] 
**install_crds** | **bool** | Installs cert-manager&#39;s resource definitions with the add-on; turn it off only if you manage them yourself. | [optional] [default to True]
**issuer_type** | [**CertManagerIssuerType**](CertManagerIssuerType.md) | Where certificates come from. Left out, it is &#x60;LetsEncrypt&#x60; once &#x60;email&#x60; is set; with no email, no issuer is created. | [optional] 

## Example

```python
from astropulse._generated.models.cert_manager_addon_configuration import CertManagerAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CertManagerAddonConfiguration from a JSON string
cert_manager_addon_configuration_instance = CertManagerAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(CertManagerAddonConfiguration.to_json())

# convert the object into a dict
cert_manager_addon_configuration_dict = cert_manager_addon_configuration_instance.to_dict()
# create an instance of CertManagerAddonConfiguration from a dict
cert_manager_addon_configuration_from_dict = CertManagerAddonConfiguration.from_dict(cert_manager_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


