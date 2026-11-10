# CertManagerAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_solver** | [**CertManagerDNSSolver**](CertManagerDNSSolver.md) | Connects the DNS zone Let&#39;s Encrypt checks ownership in. With it, certificates for applications exposed through the Ingress or the gateway are checked through DNS; without it, Ingress certificates use HTTP-01. Requires a Let&#39;s Encrypt issuer, and Identity except on an EKS cluster AstroPulse created, where both default to its Route 53 zones and its cert-manager role. | [optional] 
**email** | **str** | The contact address Let&#39;s Encrypt registers the account under and sends expiry notices to. Required when issuerType is LetsEncrypt or LetsEncryptStaging; unused for SelfSigned. | [optional] 
**enable_cluster_issuer** | **bool** | Creates AstroPulse&#39;s ClusterIssuers. Defaults to true; false installs cert-manager alone, issuing nothing. | [optional] [default to True]
**identity** | [**AddonWorkloadIdentity**](AddonWorkloadIdentity.md) | Binds cert-manager&#39;s ServiceAccount to a cloud workload identity (IRSA or Pod Identity on EKS, Workload Identity on GKE and AKS). Annotations render onto the ServiceAccount, labels onto the controller pods. Required for DNSSolver, except on an EKS cluster AstroPulse created, where it defaults to that cluster&#39;s cert-manager role. | [optional] 
**install_crds** | **bool** | Installs cert-manager&#39;s CRDs with the add-on. Defaults to true; set it false only where they are managed separately. | [optional] [default to True]
**issuer_type** | [**CertManagerIssuerType**](CertManagerIssuerType.md) | Where endpoint certificates come from. Left out, it is LetsEncrypt once &#x60;email&#x60; is set, creating both the production and the staging ClusterIssuer, and no ClusterIssuer is created without an email. | [optional] 

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


