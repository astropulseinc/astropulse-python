# GitHubPathValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | The branch the path was looked up on. | [optional] 
**message** | **str** | What was found, in a sentence. | [optional] 
**path** | **str** | The path that was looked up. | [optional] 
**repo** | **str** | The repository the path was looked up in, as owner/name. | [optional] 
**type** | [**GitHubPathType**](GitHubPathType.md) | What is at the path. | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_path_validation import GitHubPathValidation

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubPathValidation from a JSON string
git_hub_path_validation_instance = GitHubPathValidation.from_json(json)
# print the JSON string representation of the object
print(GitHubPathValidation.to_json())

# convert the object into a dict
git_hub_path_validation_dict = git_hub_path_validation_instance.to_dict()
# create an instance of GitHubPathValidation from a dict
git_hub_path_validation_from_dict = GitHubPathValidation.from_dict(git_hub_path_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


