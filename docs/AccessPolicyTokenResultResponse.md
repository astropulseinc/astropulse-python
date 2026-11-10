# AccessPolicyTokenResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccessPolicyTokenResult**](AccessPolicyTokenResult.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_token_result_response import AccessPolicyTokenResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyTokenResultResponse from a JSON string
access_policy_token_result_response_instance = AccessPolicyTokenResultResponse.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyTokenResultResponse.to_json())

# convert the object into a dict
access_policy_token_result_response_dict = access_policy_token_result_response_instance.to_dict()
# create an instance of AccessPolicyTokenResultResponse from a dict
access_policy_token_result_response_from_dict = AccessPolicyTokenResultResponse.from_dict(access_policy_token_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


