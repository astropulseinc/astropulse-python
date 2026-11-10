# CertManagerDNSSolver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosted_zone_id** | **str** | Pins the Route 53 hosted zone (&#x60;aws&#x60;). Empty lets cert-manager find the zone by name. | [optional] 
**project** | **str** | The Cloud DNS project holding the zone (&#x60;gcp&#x60;). Required for &#x60;gcp&#x60;. | [optional] 
**provider** | [**CertManagerDNSProvider**](CertManagerDNSProvider.md) | The DNS provider holding the zone: &#x60;aws&#x60;, &#x60;gcp&#x60; or &#x60;azure&#x60;. Empty selects the cluster&#39;s own provider. | [optional] 
**resource_group** | **str** | The resource group holding the Azure DNS zone. Required for &#x60;azure&#x60;. | [optional] 
**subscription_id** | **str** | The Azure subscription holding the DNS zone. Required for &#x60;azure&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.cert_manager_dns_solver import CertManagerDNSSolver

# TODO update the JSON string below
json = "{}"
# create an instance of CertManagerDNSSolver from a JSON string
cert_manager_dns_solver_instance = CertManagerDNSSolver.from_json(json)
# print the JSON string representation of the object
print(CertManagerDNSSolver.to_json())

# convert the object into a dict
cert_manager_dns_solver_dict = cert_manager_dns_solver_instance.to_dict()
# create an instance of CertManagerDNSSolver from a dict
cert_manager_dns_solver_from_dict = CertManagerDNSSolver.from_dict(cert_manager_dns_solver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


