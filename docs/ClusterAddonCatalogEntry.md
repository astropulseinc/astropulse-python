# ClusterAddonCatalogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Groups the add-on in a catalog listing. | [optional] 
**cloud_access** | [**AddonCloudAccess**](AddonCloudAccess.md) | How the add-on reaches a cloud account of yours: the account your identity must trust, and the key credentials take in a Secret. Absent for an add-on that reaches none. | [optional] 
**cluster_managed** | **bool** | Marks an add-on installed and removed with the cluster, which cannot be deleted on its own. | [optional] 
**compatible** | **bool** | Reports whether the add-on can be deployed on the cluster asked about. | [optional] 
**configuration** | [**List[AddonConfigurationField]**](AddonConfigurationField.md) | What this add-on accepts, flattened to dotted paths. Derived from the REST types themselves, so it cannot describe a setting the API would refuse or omit one it accepts. Empty for an add-on that takes no configuration. | [optional] 
**configuration_property** | **str** | The JSON property this add-on&#39;s configuration is written under, empty for one that takes none. Published because it is not derivable from the add-on&#39;s name -- workload-autoscaling is written workloadAutoscaling -- and a client building the payload from Configuration below needs the key to nest it under. | [optional] 
**dependencies** | **List[str]** | The public names of add-ons this one needs installed. | [optional] 
**description** | **str** | Says what installing it gives the cluster. | [optional] 
**display_name** | **str** | The add-on&#39;s name in front of a person. | [optional] 
**docs_url** | **str** | Where this add-on is documented, as a path relative to the documentation site. | [optional] 
**incompatibility_reason** | **str** | Says why it cannot be installed now: what rules it out when Compatible is false, or why no installable version is listed. | [optional] 
**installable_versions** | **List[str]** | The versions of this add-on that can be installed on this cluster, oldest first. Empty when none can. | [optional] 
**shared_configuration** | [**List[AddonConfigurationField]**](AddonConfigurationField.md) | What every add-on accepts, flattened to dotted paths and written directly under configuration, beside the add-on&#39;s own block. | [optional] 
**type** | [**ClusterAddonType**](ClusterAddonType.md) | The add-on&#39;s public name, and what every add-on command takes. | [optional] 
**unlocks** | **List[str]** | Says what installing this add-on makes usable, such as \&quot;model scaling on queue depth\&quot;. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_catalog_entry import ClusterAddonCatalogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonCatalogEntry from a JSON string
cluster_addon_catalog_entry_instance = ClusterAddonCatalogEntry.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonCatalogEntry.to_json())

# convert the object into a dict
cluster_addon_catalog_entry_dict = cluster_addon_catalog_entry_instance.to_dict()
# create an instance of ClusterAddonCatalogEntry from a dict
cluster_addon_catalog_entry_from_dict = ClusterAddonCatalogEntry.from_dict(cluster_addon_catalog_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


