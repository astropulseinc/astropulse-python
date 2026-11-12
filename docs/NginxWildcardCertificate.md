# NginxWildcardCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain the certificate covers, without &#x60;*.&#x60;: apps.example.com covers apps.example.com and every name directly under it. | [optional] 
**enabled** | **bool** | Issues the wildcard certificate and serves it to applications with TLS mode &#x60;Wildcard&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.nginx_wildcard_certificate import NginxWildcardCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of NginxWildcardCertificate from a JSON string
nginx_wildcard_certificate_instance = NginxWildcardCertificate.from_json(json)
# print the JSON string representation of the object
print(NginxWildcardCertificate.to_json())

# convert the object into a dict
nginx_wildcard_certificate_dict = nginx_wildcard_certificate_instance.to_dict()
# create an instance of NginxWildcardCertificate from a dict
nginx_wildcard_certificate_from_dict = NginxWildcardCertificate.from_dict(nginx_wildcard_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


