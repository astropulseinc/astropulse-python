# ApplicationProfileRequest

Application profile creation request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_tier** | [**TierType**](TierType.md) | The availability tier applications on this profile run at. | [optional] 
**cloud_provider** | [**CloudProvider**](CloudProvider.md) | Specifies the cloud provider and region for deployment (optional). If omitted, cluster selection is determined by ClusterName or platform defaults. | [optional] 
**cluster_name** | **str** | The target cluster name (optional). Takes precedence over CloudProvider when both are set. | [optional] 
**profile_name** | **str** | The profile name (required, 1-50 characters, valid DNS name). Format: lowercase alphanumeric and hyphens, must start with a letter. Example: \&quot;example-profile\&quot; | 
**resources** | [**ResourceRequirement**](ResourceRequirement.md) | Specifies resource requirements for the application. example: {\&quot;memory\&quot;:{\&quot;minimum\&quot;:\&quot;1Gi\&quot;,\&quot;maximum\&quot;:\&quot;2Gi\&quot;}} | [optional] 

## Example

```python
from astropulse._generated.models.application_profile_request import ApplicationProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProfileRequest from a JSON string
application_profile_request_instance = ApplicationProfileRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationProfileRequest.to_json())

# convert the object into a dict
application_profile_request_dict = application_profile_request_instance.to_dict()
# create an instance of ApplicationProfileRequest from a dict
application_profile_request_from_dict = ApplicationProfileRequest.from_dict(application_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


