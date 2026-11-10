# GitHubTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GitHubToken**](GitHubToken.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_token_response import GitHubTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubTokenResponse from a JSON string
git_hub_token_response_instance = GitHubTokenResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubTokenResponse.to_json())

# convert the object into a dict
git_hub_token_response_dict = git_hub_token_response_instance.to_dict()
# create an instance of GitHubTokenResponse from a dict
git_hub_token_response_from_dict = GitHubTokenResponse.from_dict(git_hub_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


