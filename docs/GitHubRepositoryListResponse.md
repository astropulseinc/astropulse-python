# GitHubRepositoryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GitHubRepository]**](GitHubRepository.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_repository_list_response import GitHubRepositoryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubRepositoryListResponse from a JSON string
git_hub_repository_list_response_instance = GitHubRepositoryListResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubRepositoryListResponse.to_json())

# convert the object into a dict
git_hub_repository_list_response_dict = git_hub_repository_list_response_instance.to_dict()
# create an instance of GitHubRepositoryListResponse from a dict
git_hub_repository_list_response_from_dict = GitHubRepositoryListResponse.from_dict(git_hub_repository_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


