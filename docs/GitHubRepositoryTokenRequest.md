# GitHubRepositoryTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_url** | **str** | The repository, as a GitHub URL. | 

## Example

```python
from astropulse._generated.models.git_hub_repository_token_request import GitHubRepositoryTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubRepositoryTokenRequest from a JSON string
git_hub_repository_token_request_instance = GitHubRepositoryTokenRequest.from_json(json)
# print the JSON string representation of the object
print(GitHubRepositoryTokenRequest.to_json())

# convert the object into a dict
git_hub_repository_token_request_dict = git_hub_repository_token_request_instance.to_dict()
# create an instance of GitHubRepositoryTokenRequest from a dict
git_hub_repository_token_request_from_dict = GitHubRepositoryTokenRequest.from_dict(git_hub_repository_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


