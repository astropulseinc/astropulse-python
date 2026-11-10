# AgentCapabilityStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The capability&#39;s name as people read it (e.g. \&quot;cost reporting\&quot;). | [optional] 
**idle** | **bool** | True when the capability is ready and has nothing on the cluster to check yet; the message says what is missing. | [optional] 
**message** | **str** | One complete sentence saying what the state means for this capability on this cluster. | [optional] 
**name** | **str** | The capability&#39;s identifier (e.g. \&quot;health-v1\&quot;). | [optional] 
**state** | [**AgentCapabilityState**](AgentCapabilityState.md) | The capability&#39;s state. A capability that is running and has no data to report yet is reported as Starting, with &#x60;waiting&#x60; set. | [optional] 
**waiting** | **bool** | True when the capability is running and is waiting for its first data. Nothing is wrong with it; the message says what it waits for. | [optional] 

## Example

```python
from astropulse._generated.models.agent_capability_status import AgentCapabilityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCapabilityStatus from a JSON string
agent_capability_status_instance = AgentCapabilityStatus.from_json(json)
# print the JSON string representation of the object
print(AgentCapabilityStatus.to_json())

# convert the object into a dict
agent_capability_status_dict = agent_capability_status_instance.to_dict()
# create an instance of AgentCapabilityStatus from a dict
agent_capability_status_from_dict = AgentCapabilityStatus.from_dict(agent_capability_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


