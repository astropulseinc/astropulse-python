# GitHubFileContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GitHubFileContent**](GitHubFileContent.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_file_content_response import GitHubFileContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubFileContentResponse from a JSON string
git_hub_file_content_response_instance = GitHubFileContentResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubFileContentResponse.to_json())

# convert the object into a dict
git_hub_file_content_response_dict = git_hub_file_content_response_instance.to_dict()
# create an instance of GitHubFileContentResponse from a dict
git_hub_file_content_response_from_dict = GitHubFileContentResponse.from_dict(git_hub_file_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


