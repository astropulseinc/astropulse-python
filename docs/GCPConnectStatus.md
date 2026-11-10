# GCPConnectStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_shell_script** | **str** | The Cloud Shell script for the setup in your project | [optional] 
**cloud_shell_script_url** | **str** | The pre-signed URL for Cloud Shell script download | [optional] 
**error** | [**Failure**](Failure.md) | Contains any error message if the request failed | [optional] 
**id** | **str** | The cloud connection ID -- the same value POST /api/v1/cloud/gcp/connect returned. Echoed so a client polling several connections can tell responses apart. | [optional] 
**last_error** | [**CloudConnectAttemptError**](CloudConnectAttemptError.md) | Why the latest check of the account failed, while one has. | [optional] 
**notice** | [**Notice**](Notice.md) | Says where the connection stands and the next step to finish it. | [optional] 
**outcome** | [**Outcome**](Outcome.md) | Blocked when connecting stopped and must be started again, and proceed otherwise. | [optional] 
**provisioner** | [**ProvisionerType**](ProvisionerType.md) | The kind of cluster the connection is for. | [optional] 
**provisioner_name** | **str** | The provisioner&#39;s name for people, such as Amazon EKS. | [optional] 
**status** | [**CloudAccountStatus**](CloudAccountStatus.md) | How far connecting the cloud account has got. It is &#x60;Ready&#x60; once connected, and &#x60;Failed&#x60; or &#x60;Denied&#x60; when the attempt stopped. | [optional] 

## Example

```python
from astropulse._generated.models.gcp_connect_status import GCPConnectStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GCPConnectStatus from a JSON string
gcp_connect_status_instance = GCPConnectStatus.from_json(json)
# print the JSON string representation of the object
print(GCPConnectStatus.to_json())

# convert the object into a dict
gcp_connect_status_dict = gcp_connect_status_instance.to_dict()
# create an instance of GCPConnectStatus from a dict
gcp_connect_status_from_dict = GCPConnectStatus.from_dict(gcp_connect_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


