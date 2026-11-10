# GitHubInstallationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GitHubInstallation**](GitHubInstallation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_installation_response import GitHubInstallationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubInstallationResponse from a JSON string
git_hub_installation_response_instance = GitHubInstallationResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubInstallationResponse.to_json())

# convert the object into a dict
git_hub_installation_response_dict = git_hub_installation_response_instance.to_dict()
# create an instance of GitHubInstallationResponse from a dict
git_hub_installation_response_from_dict = GitHubInstallationResponse.from_dict(git_hub_installation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


