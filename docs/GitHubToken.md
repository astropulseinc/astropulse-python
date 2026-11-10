# GitHubToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | When the token stops working; absent when GitHub did not say. | [optional] 
**token** | **str** | The access token to send to GitHub. Keep it secret. | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_token import GitHubToken

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubToken from a JSON string
git_hub_token_instance = GitHubToken.from_json(json)
# print the JSON string representation of the object
print(GitHubToken.to_json())

# convert the object into a dict
git_hub_token_dict = git_hub_token_instance.to_dict()
# create an instance of GitHubToken from a dict
git_hub_token_from_dict = GitHubToken.from_dict(git_hub_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


