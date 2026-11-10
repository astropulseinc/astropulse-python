# AgentCertificateBundleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AgentCertificateBundle**](AgentCertificateBundle.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.agent_certificate_bundle_response import AgentCertificateBundleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCertificateBundleResponse from a JSON string
agent_certificate_bundle_response_instance = AgentCertificateBundleResponse.from_json(json)
# print the JSON string representation of the object
print(AgentCertificateBundleResponse.to_json())

# convert the object into a dict
agent_certificate_bundle_response_dict = agent_certificate_bundle_response_instance.to_dict()
# create an instance of AgentCertificateBundleResponse from a dict
agent_certificate_bundle_response_from_dict = AgentCertificateBundleResponse.from_dict(agent_certificate_bundle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


