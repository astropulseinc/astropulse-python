# GitHubPathValidationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | The branch to look the path up on. | 
**path** | **str** | The file or directory path within the repository. | 
**repo_url** | **str** | The repository, as a GitHub URL or owner/name. | 

## Example

```python
from astropulse._generated.models.git_hub_path_validation_request import GitHubPathValidationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubPathValidationRequest from a JSON string
git_hub_path_validation_request_instance = GitHubPathValidationRequest.from_json(json)
# print the JSON string representation of the object
print(GitHubPathValidationRequest.to_json())

# convert the object into a dict
git_hub_path_validation_request_dict = git_hub_path_validation_request_instance.to_dict()
# create an instance of GitHubPathValidationRequest from a dict
git_hub_path_validation_request_from_dict = GitHubPathValidationRequest.from_dict(git_hub_path_validation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


