# ClusterExposureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterExposure**](ClusterExposure.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_exposure_response import ClusterExposureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExposureResponse from a JSON string
cluster_exposure_response_instance = ClusterExposureResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterExposureResponse.to_json())

# convert the object into a dict
cluster_exposure_response_dict = cluster_exposure_response_instance.to_dict()
# create an instance of ClusterExposureResponse from a dict
cluster_exposure_response_from_dict = ClusterExposureResponse.from_dict(cluster_exposure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


