# ExternalAccessTLS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**TLSMode**](TLSMode.md) | Certificate (a certificate issued for the endpoint&#39;s hostname), Wildcard (the nginx-ingress add-on&#39;s wildcard certificate) or Passthrough (the application serves TLS itself on its port). | [optional] 

## Example

```python
from astropulse._generated.models.external_access_tls import ExternalAccessTLS

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAccessTLS from a JSON string
external_access_tls_instance = ExternalAccessTLS.from_json(json)
# print the JSON string representation of the object
print(ExternalAccessTLS.to_json())

# convert the object into a dict
external_access_tls_dict = external_access_tls_instance.to_dict()
# create an instance of ExternalAccessTLS from a dict
external_access_tls_from_dict = ExternalAccessTLS.from_dict(external_access_tls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


