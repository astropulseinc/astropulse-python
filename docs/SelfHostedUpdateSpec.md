# SelfHostedUpdateSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_plane** | [**NodeGroup**](NodeGroup.md) | The control plane node group update configuration (optional) | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_update_spec import SelfHostedUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedUpdateSpec from a JSON string
self_hosted_update_spec_instance = SelfHostedUpdateSpec.from_json(json)
# print the JSON string representation of the object
print(SelfHostedUpdateSpec.to_json())

# convert the object into a dict
self_hosted_update_spec_dict = self_hosted_update_spec_instance.to_dict()
# create an instance of SelfHostedUpdateSpec from a dict
self_hosted_update_spec_from_dict = SelfHostedUpdateSpec.from_dict(self_hosted_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


