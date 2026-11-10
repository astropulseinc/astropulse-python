# HelmRepo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_name** | **str** | The name of the Helm chart | [optional] 
**chart_version** | **str** | The version of the Helm chart | [optional] 
**release_name** | **str** | The name of the Helm release immutable once set | [optional] 
**repo_url** | **str** | The URL of the Helm chart repository | [optional] 

## Example

```python
from astropulse._generated.models.helm_repo import HelmRepo

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRepo from a JSON string
helm_repo_instance = HelmRepo.from_json(json)
# print the JSON string representation of the object
print(HelmRepo.to_json())

# convert the object into a dict
helm_repo_dict = helm_repo_instance.to_dict()
# create an instance of HelmRepo from a dict
helm_repo_from_dict = HelmRepo.from_dict(helm_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


