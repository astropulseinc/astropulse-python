# VaultLease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The cluster a cluster-scoped credential serves. | [optional] 
**created_by** | **str** | The user who first stored it, when known. Admins only. | [optional] 
**created_by_display** | **str** | Names the user who first stored it, by name and email; empty when unknown. Admins only. | [optional] 
**expires_at** | **datetime** | When the credential expires; omitted for credentials that do not. | [optional] 
**fingerprint** | **str** | A short one-way digest of the value, for telling two credentials apart. Admins only. | [optional] 
**issued_at** | **datetime** | When the credential was first stored. | [optional] 
**kind** | [**VaultLeaseKind**](VaultLeaseKind.md) | What the credential is; absent for a kind AstroPulse no longer defines. | [optional] 
**last4** | **str** | The value&#39;s last four characters, shown only for kinds long enough that it reveals nothing. Admins only. | [optional] 
**last_validated** | **datetime** | When AstroPulse last checked the credential with its provider. | [optional] 
**last_validation** | [**VaultValidation**](VaultValidation.md) | What that check found; omitted until one has run. | [optional] 
**last_written_by** | **str** | The user who wrote it last, when known. Admins only. | [optional] 
**last_written_by_display** | **str** | Names the user who wrote it last, by name and email; empty when unknown. Admins only. | [optional] 
**lease_id** | **str** | Identifies this credential; storing a different value issues a new one. Admins only. | [optional] 
**name** | **str** | A named credential&#39;s name, such as a registry or provider. | [optional] 
**path** | **str** | Where the credential lives: org/&lt;organization&gt;/&lt;kind&gt;/&lt;scope&gt;. Admins only. | [optional] 
**producer** | **str** | The AstroPulse operation that stored it. Admins only. | [optional] 
**provisioner** | [**ProvisionerType**](ProvisionerType.md) | The kind of cluster a cloud credential serves; omitted for other credentials. | [optional] 
**provisioner_name** | **str** | The provisioner&#39;s name for people, such as Amazon EKS; omitted for other credentials. | [optional] 
**replace_command** | **str** | The astroctl command that replaces the stored value, with this credential&#39;s own values filled in; empty when not replaceable or not yet known. Admins only. | [optional] 
**replace_instruction** | **str** | Says in one sentence how to replace the stored value; empty when not replaceable. Admins only. | [optional] 
**replaceable** | **bool** | True when you can replace the stored value with a new one you made. Admins only. | [optional] 
**rotated_at** | **datetime** | When a different value last replaced the stored one. | [optional] 
**scope** | [**VaultLeaseScope**](VaultLeaseScope.md) | Whether it is the organization&#39;s one credential of its kind, one of several named ones, or one cluster&#39;s. | [optional] 
**state** | [**VaultLeaseState**](VaultLeaseState.md) | Whether AstroPulse can read the stored credential. | [optional] 
**title** | **str** | AstroPulse&#39;s name for the credential. | [optional] 
**updated_at** | **datetime** | When anything about the credential last changed. | [optional] 
**used_for** | **str** | Says in one line what the credential powers. | [optional] 
**version** | **int** | Counts the values stored under this credential; it goes up with every rotation. Admins only. | [optional] 

## Example

```python
from astropulse._generated.models.vault_lease import VaultLease

# TODO update the JSON string below
json = "{}"
# create an instance of VaultLease from a JSON string
vault_lease_instance = VaultLease.from_json(json)
# print the JSON string representation of the object
print(VaultLease.to_json())

# convert the object into a dict
vault_lease_dict = vault_lease_instance.to_dict()
# create an instance of VaultLease from a dict
vault_lease_from_dict = VaultLease.from_dict(vault_lease_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


