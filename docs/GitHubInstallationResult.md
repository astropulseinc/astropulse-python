# GitHubInstallationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_id** | **str** | The installation linked to the organization, when one was. | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_installation_result import GitHubInstallationResult

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubInstallationResult from a JSON string
git_hub_installation_result_instance = GitHubInstallationResult.from_json(json)
# print the JSON string representation of the object
print(GitHubInstallationResult.to_json())

# convert the object into a dict
git_hub_installation_result_dict = git_hub_installation_result_instance.to_dict()
# create an instance of GitHubInstallationResult from a dict
git_hub_installation_result_from_dict = GitHubInstallationResult.from_dict(git_hub_installation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


