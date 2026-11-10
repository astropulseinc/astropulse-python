# ClusterRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Failure**](Failure.md) | Contains failure details when registration fails. | [optional] 
**message** | **str** | Provides additional details. | [optional] 
**operation_id** | **str** | The unique identifier for tracking this registration operation. | [optional] 
**status** | [**ClusterStatus**](ClusterStatus.md) | The cluster&#39;s status: Registering, Registered or RegisterFailed. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_registration import ClusterRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRegistration from a JSON string
cluster_registration_instance = ClusterRegistration.from_json(json)
# print the JSON string representation of the object
print(ClusterRegistration.to_json())

# convert the object into a dict
cluster_registration_dict = cluster_registration_instance.to_dict()
# create an instance of ClusterRegistration from a dict
cluster_registration_from_dict = ClusterRegistration.from_dict(cluster_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


