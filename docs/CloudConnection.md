# CloudConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The cloud account connected; omitted for callers who are not organization admins. | [optional] 
**cluster_name** | **str** | The cluster the connection was made for. | [optional] 
**connected_at** | **str** | When the connection&#39;s setup first finished; set in the connections listing. | [optional] 
**connection_id** | **str** | The same ID the connect endpoint returns for this connection; omitted for callers who are not organization admins. | [optional] 
**created_at** | **str** | When the connection&#39;s setup started; set in the connections listing. | [optional] 
**development_credentials** | **bool** | True on a local development platform that can use this account with its own credentials, so a cluster can be created here without connecting it. State still says whether the account is connected. | [optional] 
**message** | **str** | Says what the state means. | [optional] 
**next_step** | [**NextStep**](NextStep.md) | What to do in the cloud account to reach connected, when there is a step to take; for callers who are not organization admins, it asks an admin. | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud the connection is to. | [optional] 
**provisioner** | [**ProvisionerType**](ProvisionerType.md) | The kind of cluster the connection is for; omitted when unknown. | [optional] 
**provisioner_name** | **str** | The provisioner&#39;s name for people, such as Amazon EKS; omitted when unknown. | [optional] 
**region** | **str** | The region the connection was made in; omitted for callers who are not organization admins. | [optional] 
**required_template_version** | **int** | The setup template version AstroPulse needs. | [optional] 
**resource_group** | **str** | The Azure resource group the connection was made for. | [optional] 
**setup** | [**AccountSetup**](AccountSetup.md) | The one-time setup this connection comes from. | [optional] 
**state** | [**CloudConnectionState**](CloudConnectionState.md) | How the connection stands now. | [optional] 
**template_version** | **int** | The setup template version the account runs; omitted when unknown. | [optional] 
**verified_at** | **str** | When a connection check last reached the account and got an answer. | [optional] 

## Example

```python
from astropulse._generated.models.cloud_connection import CloudConnection

# TODO update the JSON string below
json = "{}"
# create an instance of CloudConnection from a JSON string
cloud_connection_instance = CloudConnection.from_json(json)
# print the JSON string representation of the object
print(CloudConnection.to_json())

# convert the object into a dict
cloud_connection_dict = cloud_connection_instance.to_dict()
# create an instance of CloudConnection from a dict
cloud_connection_from_dict = CloudConnection.from_dict(cloud_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


