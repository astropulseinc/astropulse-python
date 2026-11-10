# ClusterVersionSupport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_version** | **str** | The oldest supported Kubernetes minor series, for example \&quot;1.34\&quot;. Omitted when the supported set is unknown. | [optional] 
**reason** | **str** | Explains the state in one sentence. | [optional] 
**state** | [**ClusterVersionSupportState**](ClusterVersionSupportState.md) | Whether AstroPulse supports the cluster&#39;s Kubernetes version. | [optional] 
**supported_versions** | **List[str]** | Lists the supported Kubernetes minor series, newest first. Omitted when the supported set is unknown. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_version_support import ClusterVersionSupport

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVersionSupport from a JSON string
cluster_version_support_instance = ClusterVersionSupport.from_json(json)
# print the JSON string representation of the object
print(ClusterVersionSupport.to_json())

# convert the object into a dict
cluster_version_support_dict = cluster_version_support_instance.to_dict()
# create an instance of ClusterVersionSupport from a dict
cluster_version_support_from_dict = ClusterVersionSupport.from_dict(cluster_version_support_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


