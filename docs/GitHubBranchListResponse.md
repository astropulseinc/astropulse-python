# GitHubBranchListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GitHubBranch]**](GitHubBranch.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_branch_list_response import GitHubBranchListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubBranchListResponse from a JSON string
git_hub_branch_list_response_instance = GitHubBranchListResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubBranchListResponse.to_json())

# convert the object into a dict
git_hub_branch_list_response_dict = git_hub_branch_list_response_instance.to_dict()
# create an instance of GitHubBranchListResponse from a dict
git_hub_branch_list_response_from_dict = GitHubBranchListResponse.from_dict(git_hub_branch_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


