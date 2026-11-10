# K8sClusterAddonManifestSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The name of the cluster the add-on runs on. | [optional] 
**configuration** | [**ClusterAddonConfiguration**](ClusterAddonConfiguration.md) | The add-on&#39;s settings. Omitted keeps the installed settings, or takes the add-on&#39;s defaults on a new install. | [optional] 
**options** | [**ClusterAddonApplyOptions**](ClusterAddonApplyOptions.md) | How the apply runs. Absent from an add-on spec read. | [optional] 
**version** | **str** | The add-on version to run. Omitted installs the default version, or keeps the installed one. | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster_addon_manifest_spec import K8sClusterAddonManifestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterAddonManifestSpec from a JSON string
k8s_cluster_addon_manifest_spec_instance = K8sClusterAddonManifestSpec.from_json(json)
# print the JSON string representation of the object
print(K8sClusterAddonManifestSpec.to_json())

# convert the object into a dict
k8s_cluster_addon_manifest_spec_dict = k8s_cluster_addon_manifest_spec_instance.to_dict()
# create an instance of K8sClusterAddonManifestSpec from a dict
k8s_cluster_addon_manifest_spec_from_dict = K8sClusterAddonManifestSpec.from_dict(k8s_cluster_addon_manifest_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


