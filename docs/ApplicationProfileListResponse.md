# ApplicationProfileListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApplicationProfile]**](ApplicationProfile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_profile_list_response import ApplicationProfileListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProfileListResponse from a JSON string
application_profile_list_response_instance = ApplicationProfileListResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationProfileListResponse.to_json())

# convert the object into a dict
application_profile_list_response_dict = application_profile_list_response_instance.to_dict()
# create an instance of ApplicationProfileListResponse from a dict
application_profile_list_response_from_dict = ApplicationProfileListResponse.from_dict(application_profile_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


