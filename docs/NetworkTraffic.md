# NetworkTraffic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incoming_rps** | **int** | Defines the inbound requests per second | [optional] [default to 10]
**outgoing_rps** | **int** | Defines the outbound requests per second If not configured, it will take the same value as IncomingRPS | [optional] 

## Example

```python
from astropulse._generated.models.network_traffic import NetworkTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkTraffic from a JSON string
network_traffic_instance = NetworkTraffic.from_json(json)
# print the JSON string representation of the object
print(NetworkTraffic.to_json())

# convert the object into a dict
network_traffic_dict = network_traffic_instance.to_dict()
# create an instance of NetworkTraffic from a dict
network_traffic_from_dict = NetworkTraffic.from_dict(network_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


