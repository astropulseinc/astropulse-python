# KubeconfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The cluster name (required, 1-50 characters, valid DNS name) | 
**credentials** | [**Credentials**](Credentials.md) | The cloud provider authentication credentials (optional). | [optional] 
**duration** | **str** | How long the kubeconfig is valid, as a duration such as 1h; one of the cluster&#39;s kubeconfigAccess.lifetimes, defaulting to its defaultLifetime. | [optional] 
**native** | **bool** | When true, returns a kubeconfig that signs in with your own cloud identity through your cloud provider&#39;s command-line tool instead of astroctl; it carries no AstroPulse credential and the response&#39;s message says what it needs. | [optional] 

## Example

```python
from astropulse._generated.models.kubeconfig_request import KubeconfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigRequest from a JSON string
kubeconfig_request_instance = KubeconfigRequest.from_json(json)
# print the JSON string representation of the object
print(KubeconfigRequest.to_json())

# convert the object into a dict
kubeconfig_request_dict = kubeconfig_request_instance.to_dict()
# create an instance of KubeconfigRequest from a dict
kubeconfig_request_from_dict = KubeconfigRequest.from_dict(kubeconfig_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


