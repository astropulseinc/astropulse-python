# CloudAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The AWS account ID, GCP project ID or Azure subscription ID; omitted for callers who are not organization admins. | [optional] 
**account_number** | **str** | The GCP project number; omitted for other clouds and for callers who are not organization admins. | [optional] 
**can_disconnect** | **bool** | True when the account has a connection, no cluster uses it and no setup is running. | [optional] 
**clusters** | [**List[CloudAccountCluster]**](CloudAccountCluster.md) | The organization&#39;s clusters in the account. | [optional] 
**connected_at** | **str** | When a connection to the account first finished its setup. | [optional] 
**disconnect_blocked_reason** | **str** | Says why the account cannot be disconnected; empty when it can. | [optional] 
**pending_connections** | [**List[CloudAccountPendingConnection]**](CloudAccountPendingConnection.md) | Connections to the account made for clusters that do not exist yet. | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud the account is in. | [optional] 
**regions** | **List[str]** | The regions the account&#39;s connections and clusters are in; omitted for callers who are not organization admins. | [optional] 
**resource_group** | **str** | The Azure resource group the account&#39;s connections were made for; omitted for callers who are not organization admins. | [optional] 
**state** | [**CloudAccountState**](CloudAccountState.md) | How the account stands now. | [optional] 
**status_message** | **str** | Says in one sentence how the account stands now. | [optional] 
**verified_at** | **str** | When a connection check last reached the account and got an answer. | [optional] 

## Example

```python
from astropulse._generated.models.cloud_account import CloudAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CloudAccount from a JSON string
cloud_account_instance = CloudAccount.from_json(json)
# print the JSON string representation of the object
print(CloudAccount.to_json())

# convert the object into a dict
cloud_account_dict = cloud_account_instance.to_dict()
# create an instance of CloudAccount from a dict
cloud_account_from_dict = CloudAccount.from_dict(cloud_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


