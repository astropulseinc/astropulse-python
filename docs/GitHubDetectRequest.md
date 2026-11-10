# GitHubDetectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh** | **bool** | Re-verifies the installations already linked and re-creates their deployment credentials. | [optional] 

## Example

```python
from astropulse._generated.models.git_hub_detect_request import GitHubDetectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubDetectRequest from a JSON string
git_hub_detect_request_instance = GitHubDetectRequest.from_json(json)
# print the JSON string representation of the object
print(GitHubDetectRequest.to_json())

# convert the object into a dict
git_hub_detect_request_dict = git_hub_detect_request_instance.to_dict()
# create an instance of GitHubDetectRequest from a dict
git_hub_detect_request_from_dict = GitHubDetectRequest.from_dict(git_hub_detect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


