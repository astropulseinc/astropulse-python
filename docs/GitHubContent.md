# GitHubContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**type** | [**GitHubContentType**](GitHubContentType.md) | What the entry is. | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_content import GitHubContent

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubContent from a JSON string
git_hub_content_instance = GitHubContent.from_json(json)
# print the JSON string representation of the object
print(GitHubContent.to_json())

# convert the object into a dict
git_hub_content_dict = git_hub_content_instance.to_dict()
# create an instance of GitHubContent from a dict
git_hub_content_from_dict = GitHubContent.from_dict(git_hub_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


