# GitHubInstallStateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GitHubInstallState**](GitHubInstallState.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_install_state_response import GitHubInstallStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubInstallStateResponse from a JSON string
git_hub_install_state_response_instance = GitHubInstallStateResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubInstallStateResponse.to_json())

# convert the object into a dict
git_hub_install_state_response_dict = git_hub_install_state_response_instance.to_dict()
# create an instance of GitHubInstallStateResponse from a dict
git_hub_install_state_response_from_dict = GitHubInstallStateResponse.from_dict(git_hub_install_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


