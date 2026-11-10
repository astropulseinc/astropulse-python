# ClusterRegistrationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_notice** | [**Notice**](Notice.md) | ConnectionReason as a notice; absent when connectionReason is empty. | [optional] 
**connection_reason** | **str** | Says why connectionStatus is not Connected when the agent is still reporting, or that the agent has not connected yet; empty otherwise. | [optional] 
**connection_status** | [**ClusterConnectivity**](ClusterConnectivity.md) | The agent&#39;s live connection state; omitted until the agent first connects. | [optional] 
**error** | [**Failure**](Failure.md) | Contains failure details when registration fails. | [optional] 
**instructions** | [**RegistrationInstructions**](RegistrationInstructions.md) | Contains setup instructions when status is ApprovalPending. | [optional] 
**last_health_check** | **str** | The timestamp of the last successful heartbeat from the agent (RFC 3339). Empty when agent has never connected. | [optional] 
**message** | **str** | Provides human-readable status details. | [optional] 
**operation_id** | **str** | The unique identifier for tracking this registration operation. | [optional] 
**status** | [**ClusterStatus**](ClusterStatus.md) | The registration&#39;s status, such as Registering, ApprovalPending, Registered or RegisterFailed. | [optional] 
**status_tone** | [**StateTone**](StateTone.md) | How status reads at a glance. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_registration_status import ClusterRegistrationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRegistrationStatus from a JSON string
cluster_registration_status_instance = ClusterRegistrationStatus.from_json(json)
# print the JSON string representation of the object
print(ClusterRegistrationStatus.to_json())

# convert the object into a dict
cluster_registration_status_dict = cluster_registration_status_instance.to_dict()
# create an instance of ClusterRegistrationStatus from a dict
cluster_registration_status_from_dict = ClusterRegistrationStatus.from_dict(cluster_registration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


