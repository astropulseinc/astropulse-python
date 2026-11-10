# GitHubDetectedInstallationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GitHubDetectedInstallations**](GitHubDetectedInstallations.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_detected_installations_response import GitHubDetectedInstallationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubDetectedInstallationsResponse from a JSON string
git_hub_detected_installations_response_instance = GitHubDetectedInstallationsResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubDetectedInstallationsResponse.to_json())

# convert the object into a dict
git_hub_detected_installations_response_dict = git_hub_detected_installations_response_instance.to_dict()
# create an instance of GitHubDetectedInstallationsResponse from a dict
git_hub_detected_installations_response_from_dict = GitHubDetectedInstallationsResponse.from_dict(git_hub_detected_installations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


