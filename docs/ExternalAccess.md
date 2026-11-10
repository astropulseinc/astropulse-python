# ExternalAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_policy_ref** | [**EndpointAccessPolicyReference**](EndpointAccessPolicyReference.md) |  | [optional] 
**access_type** | [**ExternalAccessType**](ExternalAccessType.md) | Defines the external access type | [optional] 
**dns_endpoint** | **str** | The resolved served hostname. For image and model applications it is derived from domain/hostname. For Helm and repository applications it is the hostname the chart serves, shown for reference. example: sub.domain.com | [optional] 
**domain** | **str** | (image and model applications): a verified domain to generate the app&#39;s hostname under; the app is served at &lt;app&gt;.&lt;domain&gt;. Mutually exclusive with hostname. example: example.com | [optional] 
**exposure** | [**EndpointExposure**](EndpointExposure.md) | Who can reach the endpoint: Public (from the internet) or Private (only from inside the cluster&#39;s network). Omitted takes the default of the path that serves it: the nginx-ingress or gateway add-on&#39;s exposure, or Public for a LoadBalancer. | [optional] 
**hostname** | **str** | (image and model applications): serve the app at exactly this hostname — a verified domain&#39;s apex, or a hostname under a verified domain. Mutually exclusive with domain. example: shop.example.com | [optional] 
**tls** | [**ExternalAccessTLS**](ExternalAccessTLS.md) | (applications exposed through Ingress) is how the endpoint&#39;s TLS is served. Omitted takes the default of the cluster&#39;s nginx-ingress add-on; a model application takes Certificate only. | [optional] 

## Example

```python
from astropulse._generated.models.external_access import ExternalAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAccess from a JSON string
external_access_instance = ExternalAccess.from_json(json)
# print the JSON string representation of the object
print(ExternalAccess.to_json())

# convert the object into a dict
external_access_dict = external_access_instance.to_dict()
# create an instance of ExternalAccess from a dict
external_access_from_dict = ExternalAccess.from_dict(external_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


