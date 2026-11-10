# GitHubPathValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GitHubPathValidation**](GitHubPathValidation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_path_validation_response import GitHubPathValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubPathValidationResponse from a JSON string
git_hub_path_validation_response_instance = GitHubPathValidationResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubPathValidationResponse.to_json())

# convert the object into a dict
git_hub_path_validation_response_dict = git_hub_path_validation_response_instance.to_dict()
# create an instance of GitHubPathValidationResponse from a dict
git_hub_path_validation_response_from_dict = GitHubPathValidationResponse.from_dict(git_hub_path_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


