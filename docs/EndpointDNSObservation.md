# EndpointDNSObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The IP addresses the hostname resolved to. | [optional] 
**exposure_addresses** | **List[str]** | The addresses the cluster&#39;s exposure publishes (the gateway&#39;s or the ingress controller&#39;s load balancer), the ones the hostname must point at. Empty when the exposure has no public address (NodePort). | [optional] 
**hostname** | **str** | The exposed hostname that was resolved. | [optional] 
**matches** | **bool** | Reports whether the hostname resolves to one of the exposure&#39;s addresses. Absent when there is nothing to compare: the hostname does not resolve, or the exposure publishes no address. | [optional] 
**message** | **str** | Says what could not be compared, or why. | [optional] 
**resolves** | **bool** | Reports whether the hostname resolved to at least one address. | [optional] 

## Example

```python
from astropulse._generated.models.endpoint_dns_observation import EndpointDNSObservation

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDNSObservation from a JSON string
endpoint_dns_observation_instance = EndpointDNSObservation.from_json(json)
# print the JSON string representation of the object
print(EndpointDNSObservation.to_json())

# convert the object into a dict
endpoint_dns_observation_dict = endpoint_dns_observation_instance.to_dict()
# create an instance of EndpointDNSObservation from a dict
endpoint_dns_observation_from_dict = EndpointDNSObservation.from_dict(endpoint_dns_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


