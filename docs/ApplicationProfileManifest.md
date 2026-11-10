# ApplicationProfileManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The API version. Must be \&quot;platform.astropulse.io/v1\&quot; when provided. | [optional] 
**kind** | **str** | The resource kind. Must be \&quot;ApplicationProfile\&quot; when provided. | [optional] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) | The optional manifest metadata block. When metadata.name is set and spec.profileName is omitted, metadata.name is used as the profile name. | [optional] 
**spec** | [**ApplicationProfileRequest**](ApplicationProfileRequest.md) | Contains the application profile parameters. | [optional] 

## Example

```python
from astropulse._generated.models.application_profile_manifest import ApplicationProfileManifest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProfileManifest from a JSON string
application_profile_manifest_instance = ApplicationProfileManifest.from_json(json)
# print the JSON string representation of the object
print(ApplicationProfileManifest.to_json())

# convert the object into a dict
application_profile_manifest_dict = application_profile_manifest_instance.to_dict()
# create an instance of ApplicationProfileManifest from a dict
application_profile_manifest_from_dict = ApplicationProfileManifest.from_dict(application_profile_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


