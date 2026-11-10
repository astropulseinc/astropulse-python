# SupportedK8sVersionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ami_families** | [**List[AMIFamiliesForVersion]**](AMIFamiliesForVersion.md) | Lists, for each Kubernetes minor version, the AMI families an EKS node group can use (EKS only). | [optional] 
**ami_families_notice** | [**Notice**](Notice.md) | Says why amiFamilies is absent when the AMI families could not be checked (EKS only). | [optional] 
**channel_versions** | [**Dict[str, ChannelVersions]**](ChannelVersions.md) | The versions of each GKE release channel, keyed by channel: &#x60;Stable&#x60;, &#x60;Regular&#x60; or &#x60;Rapid&#x60; (GKE only). | [optional] 
**default_version** | **str** | The version a create uses when it names none. | [optional] 
**default_version_reason** | **str** | How &#x60;defaultVersion&#x60; is chosen, in one sentence. | [optional] 
**error** | [**Failure**](Failure.md) | Contains any error message if the request failed | [optional] 
**limited_by** | [**VersionFloorSource**](VersionFloorSource.md) | What sets the oldest supported version. | [optional] 
**minimum_version** | **str** | The oldest Kubernetes minor series in supportedVersions, for example \&quot;1.34\&quot;. It summarises the list and does not replace it: a newer version is supported only if it appears in supportedVersions. | [optional] 
**supported_versions** | **List[str]** | A list of supported K8s versions in semver format | [optional] 
**upgrade_paths** | [**List[K8sUpgradePath]**](K8sUpgradePath.md) | Contains available upgrade paths from current version | [optional] 

## Example

```python
from astropulse._generated.models.supported_k8s_versions_response import SupportedK8sVersionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedK8sVersionsResponse from a JSON string
supported_k8s_versions_response_instance = SupportedK8sVersionsResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedK8sVersionsResponse.to_json())

# convert the object into a dict
supported_k8s_versions_response_dict = supported_k8s_versions_response_instance.to_dict()
# create an instance of SupportedK8sVersionsResponse from a dict
supported_k8s_versions_response_from_dict = SupportedK8sVersionsResponse.from_dict(supported_k8s_versions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


