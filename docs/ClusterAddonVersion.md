# ClusterAddonVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breaking_changes** | **List[str]** | Lists what this release changes incompatibly. It is the reason to read this list before choosing a version: add-ons run in the cluster&#39;s critical path -- NGINX carries live traffic, Karpenter owns node lifecycle -- so an upgrade is not something to pick from a version number alone. Empty means the release declares none, not that none were checked. | [optional] 
**default** | **bool** | Marks the version installed when none is named. | [optional] 
**endpoint_authentication** | **List[str]** | Lists the access-policy mechanisms this version enforces on the endpoints it routes. Empty when it enforces none. | [optional] 
**kubernetes_compatibility** | **List[str]** | Lists the Kubernetes minors this version runs on. | [optional] 
**release_date** | **datetime** | When this version was published, RFC 3339. | [optional] 
**release_notes** | **str** | Links or summarises what changed in this version. | [optional] 
**stable** | **bool** | True for a recommended or supported version, and false once it is deprecated. | [optional] 
**support** | [**ClusterAddonSupport**](ClusterAddonSupport.md) | Says whether this version is supported and until when. Absent when the version&#39;s lifecycle is not known. | [optional] 
**upstream_version** | **str** | The third-party release this version runs, such as \&quot;cert-manager v1.21.2\&quot; or \&quot;KServe v0.20.0\&quot;. Empty when there is none. | [optional] 
**version** | **str** | The add-on version, and what &#x60;apply --version&#x60; takes. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_version import ClusterAddonVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonVersion from a JSON string
cluster_addon_version_instance = ClusterAddonVersion.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonVersion.to_json())

# convert the object into a dict
cluster_addon_version_dict = cluster_addon_version_instance.to_dict()
# create an instance of ClusterAddonVersion from a dict
cluster_addon_version_from_dict = ClusterAddonVersion.from_dict(cluster_addon_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


