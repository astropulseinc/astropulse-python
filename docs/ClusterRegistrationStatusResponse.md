# ClusterRegistrationStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterRegistrationStatus**](ClusterRegistrationStatus.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_registration_status_response import ClusterRegistrationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRegistrationStatusResponse from a JSON string
cluster_registration_status_response_instance = ClusterRegistrationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterRegistrationStatusResponse.to_json())

# convert the object into a dict
cluster_registration_status_response_dict = cluster_registration_status_response_instance.to_dict()
# create an instance of ClusterRegistrationStatusResponse from a dict
cluster_registration_status_response_from_dict = ClusterRegistrationStatusResponse.from_dict(cluster_registration_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


