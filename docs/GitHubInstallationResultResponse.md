# GitHubInstallationResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GitHubInstallationResult**](GitHubInstallationResult.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_installation_result_response import GitHubInstallationResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubInstallationResultResponse from a JSON string
git_hub_installation_result_response_instance = GitHubInstallationResultResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubInstallationResultResponse.to_json())

# convert the object into a dict
git_hub_installation_result_response_dict = git_hub_installation_result_response_instance.to_dict()
# create an instance of GitHubInstallationResultResponse from a dict
git_hub_installation_result_response_from_dict = GitHubInstallationResultResponse.from_dict(git_hub_installation_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


