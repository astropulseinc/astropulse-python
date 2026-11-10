# GitHubRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_branch** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | **Dict[str, bool]** | Maps each GitHub permission (admin, maintain, push, triage, pull) to whether it is granted. | [optional] 
**private** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_repository import GitHubRepository

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubRepository from a JSON string
git_hub_repository_instance = GitHubRepository.from_json(json)
# print the JSON string representation of the object
print(GitHubRepository.to_json())

# convert the object into a dict
git_hub_repository_dict = git_hub_repository_instance.to_dict()
# create an instance of GitHubRepository from a dict
git_hub_repository_from_dict = GitHubRepository.from_dict(git_hub_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


