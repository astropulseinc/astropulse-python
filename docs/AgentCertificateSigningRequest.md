# AgentCertificateSigningRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_signing_request** | **str** | The PEM-encoded request for a P-256 ECDSA key; the names it asks for are ignored. | 

## Example

```python
from astropulse._generated.models.agent_certificate_signing_request import AgentCertificateSigningRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCertificateSigningRequest from a JSON string
agent_certificate_signing_request_instance = AgentCertificateSigningRequest.from_json(json)
# print the JSON string representation of the object
print(AgentCertificateSigningRequest.to_json())

# convert the object into a dict
agent_certificate_signing_request_dict = agent_certificate_signing_request_instance.to_dict()
# create an instance of AgentCertificateSigningRequest from a dict
agent_certificate_signing_request_from_dict = AgentCertificateSigningRequest.from_dict(agent_certificate_signing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


