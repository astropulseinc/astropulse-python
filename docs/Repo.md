# Repo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path within the repository | [optional] 
**release_name** | **str** | The name of the Helm release | [optional] 
**repo_url** | **str** | The URL of the repository | [optional] 
**target_revision** | **str** | The branch, tag, or commit SHA to use | [optional] 

## Example

```python
from astropulse._generated.models.repo import Repo

# TODO update the JSON string below
json = "{}"
# create an instance of Repo from a JSON string
repo_instance = Repo.from_json(json)
# print the JSON string representation of the object
print(Repo.to_json())

# convert the object into a dict
repo_dict = repo_instance.to_dict()
# create an instance of Repo from a dict
repo_from_dict = Repo.from_dict(repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


