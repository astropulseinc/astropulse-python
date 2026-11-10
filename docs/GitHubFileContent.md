# GitHubFileContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**repo** | **str** | The repository the file was read from, as owner/name. | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_file_content import GitHubFileContent

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubFileContent from a JSON string
git_hub_file_content_instance = GitHubFileContent.from_json(json)
# print the JSON string representation of the object
print(GitHubFileContent.to_json())

# convert the object into a dict
git_hub_file_content_dict = git_hub_file_content_instance.to_dict()
# create an instance of GitHubFileContent from a dict
git_hub_file_content_from_dict = GitHubFileContent.from_dict(git_hub_file_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


