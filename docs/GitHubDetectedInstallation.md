# GitHubDetectedInstallation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_login** | **str** |  | [optional] 
**account_type** | [**GitHubAccountType**](GitHubAccountType.md) | Whether the installation is on a personal account or an organization. | [optional] 
**installation_id** | **str** |  | [optional] 
**status** | [**GitHubInstallationStatus**](GitHubInstallationStatus.md) | Whether the installation can be used. | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_detected_installation import GitHubDetectedInstallation

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubDetectedInstallation from a JSON string
git_hub_detected_installation_instance = GitHubDetectedInstallation.from_json(json)
# print the JSON string representation of the object
print(GitHubDetectedInstallation.to_json())

# convert the object into a dict
git_hub_detected_installation_dict = git_hub_detected_installation_instance.to_dict()
# create an instance of GitHubDetectedInstallation from a dict
git_hub_detected_installation_from_dict = GitHubDetectedInstallation.from_dict(git_hub_detected_installation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


