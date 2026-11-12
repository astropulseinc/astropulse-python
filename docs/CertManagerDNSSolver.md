# CertManagerDNSSolver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosted_zone_id** | **str** | The Route 53 hosted zone to use. Left out, cert-manager finds the zone by name. | [optional] 
**project** | **str** | The Google Cloud project that holds the Cloud DNS zone. Required for &#x60;gcp&#x60;. | [optional] 
**provider** | [**CertManagerDNSProvider**](CertManagerDNSProvider.md) | The DNS service that holds the zone. Left out, it is the cluster&#39;s own cloud. | [optional] 
**resource_group** | **str** | The Azure resource group that holds the DNS zone. Required for &#x60;azure&#x60;. | [optional] 
**subscription_id** | **str** | The Azure subscription that holds the DNS zone. Required for &#x60;azure&#x60;. | [optional] 

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


