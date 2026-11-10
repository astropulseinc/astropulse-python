# ProvisionerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator_min_kubernetes_version** | **str** | The lowest Kubernetes version (major.minor) a cluster with an accelerator node group may run; set when AcceleratorNodeGroups is true. | [optional] 
**accelerator_node_groups** | **bool** | True when a node group may carry an accelerator (a GPU) on this provisioner. | [optional] 
**account_setup** | [**AccountSetup**](AccountSetup.md) | Names that setup when NeedsAccountSetup is true. | [optional] 
**creates_clusters** | **bool** | False for a provisioner that joins a cluster you already run instead of creating one. | [optional] 
**display_name** | **str** | The provisioner&#39;s name for people. | [optional] 
**docs_path** | **str** | The documentation page for the provisioner, relative to the site root. | [optional] 
**needs_account_setup** | **bool** | True when the account needs a one-time setup before the first cluster. | [optional] 
**settings** | [**List[SettingOptions]**](SettingOptions.md) | The cluster and node group fields this provisioner offers, each with the values or the form of value it accepts; absent when the provisioner does not create clusters. | [optional] 
**summary** | **str** | Says in one line who runs the control plane and what you manage. | [optional] 
**type** | [**ProvisionerType**](ProvisionerType.md) | The value for provisioner.type in a cluster spec. | [optional] 

## Example

```python
from astropulse._generated.models.provisioner_info import ProvisionerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionerInfo from a JSON string
provisioner_info_instance = ProvisionerInfo.from_json(json)
# print the JSON string representation of the object
print(ProvisionerInfo.to_json())

# convert the object into a dict
provisioner_info_dict = provisioner_info_instance.to_dict()
# create an instance of ProvisionerInfo from a dict
provisioner_info_from_dict = ProvisionerInfo.from_dict(provisioner_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


