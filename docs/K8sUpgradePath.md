# K8sUpgradePath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_version** | **str** | The source version | [optional] 
**to_version** | **str** | The target version | [optional] 
**upgrade_type** | [**UpgradeKind**](UpgradeKind.md) | How far the upgrade moves the Kubernetes version. | [optional] 
**warnings** | **List[str]** | Contain any warnings or notes about this upgrade path | [optional] 

## Example

```python
from astropulse._generated.models.k8s_upgrade_path import K8sUpgradePath

# TODO update the JSON string below
json = "{}"
# create an instance of K8sUpgradePath from a JSON string
k8s_upgrade_path_instance = K8sUpgradePath.from_json(json)
# print the JSON string representation of the object
print(K8sUpgradePath.to_json())

# convert the object into a dict
k8s_upgrade_path_dict = k8s_upgrade_path_instance.to_dict()
# create an instance of K8sUpgradePath from a dict
k8s_upgrade_path_from_dict = K8sUpgradePath.from_dict(k8s_upgrade_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


