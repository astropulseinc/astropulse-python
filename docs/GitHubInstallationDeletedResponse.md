# GitHubInstallationDeletedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GitHubInstallationDeleted**](GitHubInstallationDeleted.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_installation_deleted_response import GitHubInstallationDeletedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubInstallationDeletedResponse from a JSON string
git_hub_installation_deleted_response_instance = GitHubInstallationDeletedResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubInstallationDeletedResponse.to_json())

# convert the object into a dict
git_hub_installation_deleted_response_dict = git_hub_installation_deleted_response_instance.to_dict()
# create an instance of GitHubInstallationDeletedResponse from a dict
git_hub_installation_deleted_response_from_dict = GitHubInstallationDeletedResponse.from_dict(git_hub_installation_deleted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


