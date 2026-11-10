# AgentCertificateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** | The RFC 3339 time the certificate expires. | [optional] 
**notice** | [**Notice**](Notice.md) | What this means and what to do, when the certificate is expiring or expired. | [optional] 
**state** | [**AgentCertificateState**](AgentCertificateState.md) | Whether the certificate is still good, about to expire or expired. | [optional] 

## Example

```python
from astropulse._generated.models.agent_certificate_status import AgentCertificateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCertificateStatus from a JSON string
agent_certificate_status_instance = AgentCertificateStatus.from_json(json)
# print the JSON string representation of the object
print(AgentCertificateStatus.to_json())

# convert the object into a dict
agent_certificate_status_dict = agent_certificate_status_instance.to_dict()
# create an instance of AgentCertificateStatus from a dict
agent_certificate_status_from_dict = AgentCertificateStatus.from_dict(agent_certificate_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


