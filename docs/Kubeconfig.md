# Kubeconfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_auth_type** | [**KubeClientAuth**](KubeClientAuth.md) | How it authenticates to the cluster. | [optional] 
**data** | **str** | The kubeconfig itself. | [optional] 
**duration** | **str** | How long it stays valid, as a Go duration such as 24h. | [optional] 
**env_vars** | **Dict[str, str]** | The environment variables an exec-based kubeconfig needs. | [optional] 
**last_updated_timestamp** | **str** | When it was last regenerated. | [optional] 
**not_after_timestamp** | **str** | When it stops. | [optional] 
**not_before_timestamp** | **str** | When it starts being valid. | [optional] 

## Example

```python
from astropulse._generated.models.kubeconfig import Kubeconfig

# TODO update the JSON string below
json = "{}"
# create an instance of Kubeconfig from a JSON string
kubeconfig_instance = Kubeconfig.from_json(json)
# print the JSON string representation of the object
print(Kubeconfig.to_json())

# convert the object into a dict
kubeconfig_dict = kubeconfig_instance.to_dict()
# create an instance of Kubeconfig from a dict
kubeconfig_from_dict = Kubeconfig.from_dict(kubeconfig_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


