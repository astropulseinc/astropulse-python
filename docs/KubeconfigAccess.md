# KubeconfigAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_lifetime** | **str** | The lifetime a kubeconfig gets when none is chosen. | [optional] 
**lifetimes** | **List[str]** | The validity periods a generated kubeconfig can be given, as durations such as 1h. | [optional] 
**note** | **str** | Says in one sentence how the kubeconfig signs in. | [optional] 

## Example

```python
from astropulse._generated.models.kubeconfig_access import KubeconfigAccess

# TODO update the JSON string below
json = "{}"
# create an instance of KubeconfigAccess from a JSON string
kubeconfig_access_instance = KubeconfigAccess.from_json(json)
# print the JSON string representation of the object
print(KubeconfigAccess.to_json())

# convert the object into a dict
kubeconfig_access_dict = kubeconfig_access_instance.to_dict()
# create an instance of KubeconfigAccess from a dict
kubeconfig_access_from_dict = KubeconfigAccess.from_dict(kubeconfig_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


