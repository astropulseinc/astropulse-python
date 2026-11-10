# GitHubBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**GitHubBranchCommit**](GitHubBranchCommit.md) |  | [optional] 
**name** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_branch import GitHubBranch

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubBranch from a JSON string
git_hub_branch_instance = GitHubBranch.from_json(json)
# print the JSON string representation of the object
print(GitHubBranch.to_json())

# convert the object into a dict
git_hub_branch_dict = git_hub_branch_instance.to_dict()
# create an instance of GitHubBranch from a dict
git_hub_branch_from_dict = GitHubBranch.from_dict(git_hub_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


