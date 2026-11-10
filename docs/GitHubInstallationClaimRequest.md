# GitHubInstallationClaimRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_user_token** | **str** | The person&#39;s GitHub user access token, used to confirm they can access the installation. It is not stored. | 
**installation_id** | **str** | The GitHub App installation to link, as digits. | 

## Example

```python
from astropulse._generated.models.git_hub_installation_claim_request import GitHubInstallationClaimRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubInstallationClaimRequest from a JSON string
git_hub_installation_claim_request_instance = GitHubInstallationClaimRequest.from_json(json)
# print the JSON string representation of the object
print(GitHubInstallationClaimRequest.to_json())

# convert the object into a dict
git_hub_installation_claim_request_dict = git_hub_installation_claim_request_instance.to_dict()
# create an instance of GitHubInstallationClaimRequest from a dict
git_hub_installation_claim_request_from_dict = GitHubInstallationClaimRequest.from_dict(git_hub_installation_claim_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


