# AKSUpdateSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acr_resource_ids** | **List[str]** | Replaces the registries the cluster pulls from with no credential (optional, max 20): added ones get AcrPull, removed ones lose it. Omit to keep them. | [optional] 
**authorized_ip_ranges** | **List[str]** | CIDR blocks that restrict API server access (optional, max 200 entries). Each entry must be a valid CIDR block. Not supported for private clusters. | [optional] 
**auto_upgrade_channel** | [**AKSAutoUpgradeChannel**](AKSAutoUpgradeChannel.md) | How the cluster upgrades its Kubernetes version. Omitted keeps it. | [optional] 
**credentials** | [**Credentials**](Credentials.md) | Replaces the cluster&#39;s stored static credentials when it carries data; omitted, or with the type and no data, it keeps them. | [optional] 
**node_os_upgrade_channel** | [**AKSNodeOSUpgradeChannel**](AKSNodeOSUpgradeChannel.md) | How the cluster updates its nodes&#39; operating system. Omitted keeps it. | [optional] 

## Example

```python
from astropulse._generated.models.aks_update_spec import AKSUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AKSUpdateSpec from a JSON string
aks_update_spec_instance = AKSUpdateSpec.from_json(json)
# print the JSON string representation of the object
print(AKSUpdateSpec.to_json())

# convert the object into a dict
aks_update_spec_dict = aks_update_spec_instance.to_dict()
# create an instance of AKSUpdateSpec from a dict
aks_update_spec_from_dict = AKSUpdateSpec.from_dict(aks_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


