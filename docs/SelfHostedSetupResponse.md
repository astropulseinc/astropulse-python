# SelfHostedSetupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SelfHostedSetup**](SelfHostedSetup.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_setup_response import SelfHostedSetupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedSetupResponse from a JSON string
self_hosted_setup_response_instance = SelfHostedSetupResponse.from_json(json)
# print the JSON string representation of the object
print(SelfHostedSetupResponse.to_json())

# convert the object into a dict
self_hosted_setup_response_dict = self_hosted_setup_response_instance.to_dict()
# create an instance of SelfHostedSetupResponse from a dict
self_hosted_setup_response_from_dict = SelfHostedSetupResponse.from_dict(self_hosted_setup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


