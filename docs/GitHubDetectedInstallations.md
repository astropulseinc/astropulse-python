# GitHubDetectedInstallations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | [**List[GitHubDetectedInstallation]**](GitHubDetectedInstallation.md) |  | [optional] 
**linked** | [**List[GitHubDetectedInstallation]**](GitHubDetectedInstallation.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_detected_installations import GitHubDetectedInstallations

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubDetectedInstallations from a JSON string
git_hub_detected_installations_instance = GitHubDetectedInstallations.from_json(json)
# print the JSON string representation of the object
print(GitHubDetectedInstallations.to_json())

# convert the object into a dict
git_hub_detected_installations_dict = git_hub_detected_installations_instance.to_dict()
# create an instance of GitHubDetectedInstallations from a dict
git_hub_detected_installations_from_dict = GitHubDetectedInstallations.from_dict(git_hub_detected_installations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


