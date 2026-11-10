# ApplicationProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The name of the cluster. | [optional] 
**cluster_selection** | [**ClusterSelection**](ClusterSelection.md) |  | [optional] 
**constraints** | [**Constraints**](Constraints.md) | Specifies different constraint that the underlying infrastructe has to adhere to run the application. | [optional] 
**id** | **str** | The unique identifier of the application profile. | [optional] 
**name** | **str** | The name of the application profile. | [optional] 
**namespace** | **str** | The Kubernetes namespace where the profile resides. | [optional] 
**org_id** | **str** | The organization ID. | [optional] 
**slug** | **str** | The unique identifier of the application profile. | [optional] 

## Example

```python
from astropulse._generated.models.application_profile import ApplicationProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProfile from a JSON string
application_profile_instance = ApplicationProfile.from_json(json)
# print the JSON string representation of the object
print(ApplicationProfile.to_json())

# convert the object into a dict
application_profile_dict = application_profile_instance.to_dict()
# create an instance of ApplicationProfile from a dict
application_profile_from_dict = ApplicationProfile.from_dict(application_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


