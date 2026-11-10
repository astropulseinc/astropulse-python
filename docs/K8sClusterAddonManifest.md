# K8sClusterAddonManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The API version, &#x60;platform.astropulse.io/v1&#x60;. | [optional] 
**kind** | **str** | The resource kind, &#x60;K8sClusterAddon&#x60;. | [optional] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) | The manifest metadata; &#x60;metadata.name&#x60; is the add-on type, such as &#x60;cert-manager&#x60;. | [optional] 
**spec** | [**K8sClusterAddonManifestSpec**](K8sClusterAddonManifestSpec.md) | The add-on&#39;s desired state on one cluster. | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster_addon_manifest import K8sClusterAddonManifest

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterAddonManifest from a JSON string
k8s_cluster_addon_manifest_instance = K8sClusterAddonManifest.from_json(json)
# print the JSON string representation of the object
print(K8sClusterAddonManifest.to_json())

# convert the object into a dict
k8s_cluster_addon_manifest_dict = k8s_cluster_addon_manifest_instance.to_dict()
# create an instance of K8sClusterAddonManifest from a dict
k8s_cluster_addon_manifest_from_dict = K8sClusterAddonManifest.from_dict(k8s_cluster_addon_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


