# GitHubInstallState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | When the install must be completed by. | [optional] 
**state** | **str** | Returned unchanged by GitHub and sent back on the installation callback. | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_install_state import GitHubInstallState

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubInstallState from a JSON string
git_hub_install_state_instance = GitHubInstallState.from_json(json)
# print the JSON string representation of the object
print(GitHubInstallState.to_json())

# convert the object into a dict
git_hub_install_state_dict = git_hub_install_state_instance.to_dict()
# create an instance of GitHubInstallState from a dict
git_hub_install_state_from_dict = GitHubInstallState.from_dict(git_hub_install_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


