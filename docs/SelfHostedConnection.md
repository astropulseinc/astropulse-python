# SelfHostedConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The cluster name | [optional] 
**error** | [**Failure**](Failure.md) | Contains any error message if the request failed | [optional] 
**message** | **str** | Says what was stored and, after a replace, which key is still valid in the cloud account and the command that deletes it there. | [optional] 
**setup** | [**SelfHostedSetup**](SelfHostedSetup.md) | The cluster&#39;s recorded setup, with the check and store steps this request ran. | [optional] 
**status** | [**SelfHostedCredentialState**](SelfHostedCredentialState.md) | How the stored credentials stand. | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_connection import SelfHostedConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedConnection from a JSON string
self_hosted_connection_instance = SelfHostedConnection.from_json(json)
# print the JSON string representation of the object
print(SelfHostedConnection.to_json())

# convert the object into a dict
self_hosted_connection_dict = self_hosted_connection_instance.to_dict()
# create an instance of SelfHostedConnection from a dict
self_hosted_connection_from_dict = SelfHostedConnection.from_dict(self_hosted_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


