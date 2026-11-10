# AccessPolicyTokenResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** |  | [optional] 
**message** | **str** | Explains the reason in words. | [optional] 
**notice** | [**Notice**](Notice.md) | Says what happened and the one thing to do, for a refusal that has a next step. | [optional] 
**reason** | [**AccessPolicyTokenRejection**](AccessPolicyTokenRejection.md) | Why the token was refused; empty when it was accepted. | [optional] 
**response_body** | **str** | The plain-text body of that answer, word for word. | [optional] 
**response_status** | **int** | The HTTP status an endpoint using the policy answers a request carrying this token with: 401 or 403. Omitted when the token is accepted, or when the identity provider&#39;s key set could not be read. | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_token_result import AccessPolicyTokenResult

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyTokenResult from a JSON string
access_policy_token_result_instance = AccessPolicyTokenResult.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyTokenResult.to_json())

# convert the object into a dict
access_policy_token_result_dict = access_policy_token_result_instance.to_dict()
# create an instance of AccessPolicyTokenResult from a dict
access_policy_token_result_from_dict = AccessPolicyTokenResult.from_dict(access_policy_token_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


