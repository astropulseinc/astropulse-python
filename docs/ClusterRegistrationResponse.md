# ClusterRegistrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterRegistration**](ClusterRegistration.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_registration_response import ClusterRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRegistrationResponse from a JSON string
cluster_registration_response_instance = ClusterRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterRegistrationResponse.to_json())

# convert the object into a dict
cluster_registration_response_dict = cluster_registration_response_instance.to_dict()
# create an instance of ClusterRegistrationResponse from a dict
cluster_registration_response_from_dict = ClusterRegistrationResponse.from_dict(cluster_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


