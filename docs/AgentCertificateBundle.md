# AgentCertificateBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate** | **str** | The PEM-encoded certificate authority the agent trusts. | [optional] 
**certificate** | **str** | The PEM-encoded certificate. | [optional] 
**expires_at** | **str** | The RFC 3339 time the certificate expires. | [optional] 
**namespace** | **str** | The namespace of the agent&#39;s TLS Secret. | [optional] 
**previous_certificate_accepted_until** | **str** | The RFC 3339 time the agent&#39;s current certificate stops being accepted, unless the agent connects with this one first; empty when the agent had none. | [optional] 
**secret_name** | **str** | The name of the agent&#39;s TLS Secret. | [optional] 

## Example

```python
from astropulse._generated.models.agent_certificate_bundle import AgentCertificateBundle

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCertificateBundle from a JSON string
agent_certificate_bundle_instance = AgentCertificateBundle.from_json(json)
# print the JSON string representation of the object
print(AgentCertificateBundle.to_json())

# convert the object into a dict
agent_certificate_bundle_dict = agent_certificate_bundle_instance.to_dict()
# create an instance of AgentCertificateBundle from a dict
agent_certificate_bundle_from_dict = AgentCertificateBundle.from_dict(agent_certificate_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


