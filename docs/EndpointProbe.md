# EndpointProbe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**reach** | [**EndpointProbeReach**](EndpointProbeReach.md) | What the endpoint&#39;s hostname did when tried from inside the cluster. | [optional] 
**result** | [**EndpointProbeResult**](EndpointProbeResult.md) | What the probe found. | [optional] 
**vantage** | [**EndpointProbeVantage**](EndpointProbeVantage.md) | Where the probe was sent from. | [optional] 

## Example

```python
from astropulse._generated.models.endpoint_probe import EndpointProbe

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointProbe from a JSON string
endpoint_probe_instance = EndpointProbe.from_json(json)
# print the JSON string representation of the object
print(EndpointProbe.to_json())

# convert the object into a dict
endpoint_probe_dict = endpoint_probe_instance.to_dict()
# create an instance of EndpointProbe from a dict
endpoint_probe_from_dict = EndpointProbe.from_dict(endpoint_probe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


