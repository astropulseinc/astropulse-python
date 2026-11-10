# EndpointExposureStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exposure** | [**EndpointExposure**](EndpointExposure.md) | Who can reach the endpoint. | [optional] 
**label** | **str** | The exposure for display. | [optional] 
**note** | **str** | A sentence about the load balancer behind the endpoint, for example that it is a Network Load Balancer on AWS. | [optional] 
**reachability** | **str** | Says in one sentence who can reach the endpoint. | [optional] 
**source** | [**ExposureSource**](ExposureSource.md) | Whether the application names its exposure or takes the cluster&#39;s default. | [optional] 

## Example

```python
from astropulse._generated.models.endpoint_exposure_status import EndpointExposureStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointExposureStatus from a JSON string
endpoint_exposure_status_instance = EndpointExposureStatus.from_json(json)
# print the JSON string representation of the object
print(EndpointExposureStatus.to_json())

# convert the object into a dict
endpoint_exposure_status_dict = endpoint_exposure_status_instance.to_dict()
# create an instance of EndpointExposureStatus from a dict
endpoint_exposure_status_from_dict = EndpointExposureStatus.from_dict(endpoint_exposure_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


