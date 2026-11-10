# GitHubInstallation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the GitHub account the installation is on. | [optional] 
**account_login** | **str** | The login of the GitHub account the installation is on. | [optional] 
**account_type** | [**GitHubAccountType**](GitHubAccountType.md) | Whether the installation is on a personal account or an organization. | [optional] 
**created_at** | **str** | When the installation was first linked. | [optional] 
**created_by_user_id** | **str** | The user who linked the installation. | [optional] 
**id** | **str** | The installation&#39;s ID on GitHub. | [optional] 
**linked_elsewhere** | **bool** | Whether the installation is also linked to at least one other organization. | [optional] 
**organization_id** | **str** | The organization the installation is linked to. | [optional] 
**status** | [**GitHubInstallationStatus**](GitHubInstallationStatus.md) | Whether the installation can be used. | [optional] 
**suspended_at** | **str** | When GitHub suspended the installation, if it is suspended. | [optional] 
**updated_at** | **str** | When the installation was last changed. | [optional] 
**updated_by_user_id** | **str** | The user who last changed the installation. | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_installation import GitHubInstallation

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubInstallation from a JSON string
git_hub_installation_instance = GitHubInstallation.from_json(json)
# print the JSON string representation of the object
print(GitHubInstallation.to_json())

# convert the object into a dict
git_hub_installation_dict = git_hub_installation_instance.to_dict()
# create an instance of GitHubInstallation from a dict
git_hub_installation_from_dict = GitHubInstallation.from_dict(git_hub_installation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


