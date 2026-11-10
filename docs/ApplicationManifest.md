# ApplicationManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The API version. Must be \&quot;platform.astropulse.io/v1\&quot; when provided. | [optional] 
**kind** | **str** | The resource kind. Must be \&quot;Application\&quot; when provided. | [optional] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) | The optional manifest metadata block. When metadata.name is set and spec.name is omitted, metadata.name is used as the application name. | [optional] 
**spec** | [**ApplicationRequest**](ApplicationRequest.md) | Contains the application deployment parameters. | [optional] 

## Example

```python
from astropulse._generated.models.application_manifest import ApplicationManifest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationManifest from a JSON string
application_manifest_instance = ApplicationManifest.from_json(json)
# print the JSON string representation of the object
print(ApplicationManifest.to_json())

# convert the object into a dict
application_manifest_dict = application_manifest_instance.to_dict()
# create an instance of ApplicationManifest from a dict
application_manifest_from_dict = ApplicationManifest.from_dict(application_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


