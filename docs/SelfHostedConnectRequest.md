# SelfHostedConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The cloud account or project ID (required) | 
**bucket_name** | **str** | The state store bucket name. Defaults to the bucket setup creates for the cluster. | [optional] 
**cluster_name** | **str** | The cluster name (required, 1-50 characters, valid DNS name) | 
**credentials** | **Dict[str, str]** | Contains the cloud provider credential key-value pairs (required) | 
**force_update** | **bool** | Overwrites existing vault credentials if true | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud the self-hosted cluster runs in. | 
**region** | **str** | The cloud region (required) | 
**without_setup** | **bool** | Stores credentials you made yourself when no setup was started for the cluster in this organization. Without it, only the credentials the cluster&#39;s setup created are stored. | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_connect_request import SelfHostedConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedConnectRequest from a JSON string
self_hosted_connect_request_instance = SelfHostedConnectRequest.from_json(json)
# print the JSON string representation of the object
print(SelfHostedConnectRequest.to_json())

# convert the object into a dict
self_hosted_connect_request_dict = self_hosted_connect_request_instance.to_dict()
# create an instance of SelfHostedConnectRequest from a dict
self_hosted_connect_request_from_dict = SelfHostedConnectRequest.from_dict(self_hosted_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


