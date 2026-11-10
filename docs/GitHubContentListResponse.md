# GitHubContentListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GitHubContent]**](GitHubContent.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_content_list_response import GitHubContentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubContentListResponse from a JSON string
git_hub_content_list_response_instance = GitHubContentListResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubContentListResponse.to_json())

# convert the object into a dict
git_hub_content_list_response_dict = git_hub_content_list_response_instance.to_dict()
# create an instance of GitHubContentListResponse from a dict
git_hub_content_list_response_from_dict = GitHubContentListResponse.from_dict(git_hub_content_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


