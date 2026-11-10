# EndpointStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_origins** | [**List[EndpointOrigin]**](EndpointOrigin.md) | The websites whose pages can call the endpoint from a browser, each with where it comes from. Reported only while URL is reported. | [optional] 
**application** | **str** |  | [optional] 
**cluster** | **str** |  | [optional] 
**desired_state** | [**EndpointDesiredState**](EndpointDesiredState.md) |  | [optional] 
**dns** | [**EndpointDNSObservation**](EndpointDNSObservation.md) | What AstroPulse observed of the endpoint&#39;s hostname: whether it resolves, and whether that is the address the cluster&#39;s gateway publishes. Only reported while URL is reported. | [optional] 
**generation** | **int** |  | [optional] 
**message** | **str** | Says in plain words why the endpoint is Pending or in Error, or on Ready what a caller must send, how far its address was checked and any warning about it. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | What to do about the endpoint&#39;s state, each with its next step. | [optional] 
**observed_at** | **str** |  | [optional] 
**phase** | [**EndpointPhase**](EndpointPhase.md) |  | [optional] 
**policy** | **str** |  | [optional] 
**policy_revision** | **int** |  | [optional] 
**probe** | [**EndpointProbe**](EndpointProbe.md) |  | [optional] 
**url** | **str** | The address to call. It is shown while the endpoint is open and Ready, and is empty otherwise; message says how far the address was checked. | [optional] 

## Example

```python
from astropulse._generated.models.endpoint_status import EndpointStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStatus from a JSON string
endpoint_status_instance = EndpointStatus.from_json(json)
# print the JSON string representation of the object
print(EndpointStatus.to_json())

# convert the object into a dict
endpoint_status_dict = endpoint_status_instance.to_dict()
# create an instance of EndpointStatus from a dict
endpoint_status_from_dict = EndpointStatus.from_dict(endpoint_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


