# K8sVersionAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breaking_changes** | **List[str]** |  | [optional] 
**current_version** | **str** |  | [optional] 
**deprecated_apis** | **List[str]** |  | [optional] 
**skipped_versions** | **List[str]** |  | [optional] 
**target_version** | **str** |  | [optional] 
**upgrade_type** | [**UpgradeKind**](UpgradeKind.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.k8s_version_analysis import K8sVersionAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of K8sVersionAnalysis from a JSON string
k8s_version_analysis_instance = K8sVersionAnalysis.from_json(json)
# print the JSON string representation of the object
print(K8sVersionAnalysis.to_json())

# convert the object into a dict
k8s_version_analysis_dict = k8s_version_analysis_instance.to_dict()
# create an instance of K8sVersionAnalysis from a dict
k8s_version_analysis_from_dict = K8sVersionAnalysis.from_dict(k8s_version_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


