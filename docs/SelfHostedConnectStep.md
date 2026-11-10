# SelfHostedConnectStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The astroctl command to run. | [optional] 
**instructions** | **str** | Says where to run the command and what it does. | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_connect_step import SelfHostedConnectStep

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedConnectStep from a JSON string
self_hosted_connect_step_instance = SelfHostedConnectStep.from_json(json)
# print the JSON string representation of the object
print(SelfHostedConnectStep.to_json())

# convert the object into a dict
self_hosted_connect_step_dict = self_hosted_connect_step_instance.to_dict()
# create an instance of SelfHostedConnectStep from a dict
self_hosted_connect_step_from_dict = SelfHostedConnectStep.from_dict(self_hosted_connect_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


