# ApplicationProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationProfile**](ApplicationProfile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_profile_response import ApplicationProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProfileResponse from a JSON string
application_profile_response_instance = ApplicationProfileResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationProfileResponse.to_json())

# convert the object into a dict
application_profile_response_dict = application_profile_response_instance.to_dict()
# create an instance of ApplicationProfileResponse from a dict
application_profile_response_from_dict = ApplicationProfileResponse.from_dict(application_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


