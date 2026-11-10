# AccessPolicyAPIKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** | Where callers send the key: Authorization (the default) or x-api-key. | [optional] 
**managed** | **bool** | Keeps the policy&#39;s keys in AstroPulse, where you create, list and revoke them. | [optional] 
**secret_ref** | [**AccessPolicySecretRef**](AccessPolicySecretRef.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_api_keys import AccessPolicyAPIKeys

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyAPIKeys from a JSON string
access_policy_api_keys_instance = AccessPolicyAPIKeys.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyAPIKeys.to_json())

# convert the object into a dict
access_policy_api_keys_dict = access_policy_api_keys_instance.to_dict()
# create an instance of AccessPolicyAPIKeys from a dict
access_policy_api_keys_from_dict = AccessPolicyAPIKeys.from_dict(access_policy_api_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


