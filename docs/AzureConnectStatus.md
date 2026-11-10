# AzureConnectStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Failure**](Failure.md) | Contains any error message if the request failed | [optional] 
**id** | **str** | The cloud connection ID -- the same value POST /api/v1/cloud/azure/connect returned. Echoed so a client polling several connections can tell responses apart. | [optional] 
**last_error** | [**CloudConnectAttemptError**](CloudConnectAttemptError.md) | Why the latest check of the account failed, while one has. | [optional] 
**notice** | [**Notice**](Notice.md) | Says where the connection stands and the next step to finish it. | [optional] 
**outcome** | [**Outcome**](Outcome.md) | Blocked when connecting stopped and must be started again, and proceed otherwise. | [optional] 
**provisioner** | [**ProvisionerType**](ProvisionerType.md) | The kind of cluster the connection is for. | [optional] 
**provisioner_name** | **str** | The provisioner&#39;s name for people, such as Amazon EKS. | [optional] 
**setup_script** | **str** | The generated Azure Cloud Shell setup script | [optional] 
**setup_script_url** | **str** | An optional pre-signed URL for the setup script | [optional] 
**status** | [**CloudAccountStatus**](CloudAccountStatus.md) | How far connecting the cloud account has got. It is &#x60;Ready&#x60; once connected, and &#x60;Failed&#x60; or &#x60;Denied&#x60; when the attempt stopped. | [optional] 
**tenant_id** | **str** | The Microsoft Entra directory (tenant) ID that owns the subscription, where Azure Cloud Shell must be signed in to run the setup. Empty when it could not be determined. | [optional] 

## Example

```python
from astropulse._generated.models.azure_connect_status import AzureConnectStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AzureConnectStatus from a JSON string
azure_connect_status_instance = AzureConnectStatus.from_json(json)
# print the JSON string representation of the object
print(AzureConnectStatus.to_json())

# convert the object into a dict
azure_connect_status_dict = azure_connect_status_instance.to_dict()
# create an instance of AzureConnectStatus from a dict
azure_connect_status_from_dict = AzureConnectStatus.from_dict(azure_connect_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


