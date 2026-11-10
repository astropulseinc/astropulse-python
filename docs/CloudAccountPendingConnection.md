# CloudAccountPendingConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The cluster the connection was made for. | [optional] 
**connection_id** | **str** | The ID the connect endpoint returned; omitted for callers who are not organization admins. | [optional] 
**last_error** | **str** | Why the latest setup did not finish; omitted for callers who are not organization admins. | [optional] 
**message** | **str** | Says in one sentence how the connection stands and that its cluster does not exist yet. | [optional] 
**provisioner** | [**ProvisionerType**](ProvisionerType.md) | The kind of cluster the connection was made for; omitted when unknown. | [optional] 
**provisioner_name** | **str** | The provisioner&#39;s name for people, such as Amazon EKS; omitted when unknown. | [optional] 
**started_at** | **str** | When the connection&#39;s latest setup started. | [optional] 
**state** | [**CloudConnectionState**](CloudConnectionState.md) | How the connection stands now. | [optional] 

## Example

```python
from astropulse._generated.models.cloud_account_pending_connection import CloudAccountPendingConnection

# TODO update the JSON string below
json = "{}"
# create an instance of CloudAccountPendingConnection from a JSON string
cloud_account_pending_connection_instance = CloudAccountPendingConnection.from_json(json)
# print the JSON string representation of the object
print(CloudAccountPendingConnection.to_json())

# convert the object into a dict
cloud_account_pending_connection_dict = cloud_account_pending_connection_instance.to_dict()
# create an instance of CloudAccountPendingConnection from a dict
cloud_account_pending_connection_from_dict = CloudAccountPendingConnection.from_dict(cloud_account_pending_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


