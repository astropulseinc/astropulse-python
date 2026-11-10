# AccessPolicySpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_origins** | **List[str]** | Websites whose pages may call endpoints that use this policy from a browser, each as an origin such as https://app.example.com. Empty means no browser access from other sites. | [optional] 
**api_keys** | [**AccessPolicyAPIKeys**](AccessPolicyAPIKeys.md) |  | [optional] 
**jwt** | [**AccessPolicyJWT**](AccessPolicyJWT.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_spec import AccessPolicySpec

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicySpec from a JSON string
access_policy_spec_instance = AccessPolicySpec.from_json(json)
# print the JSON string representation of the object
print(AccessPolicySpec.to_json())

# convert the object into a dict
access_policy_spec_dict = access_policy_spec_instance.to_dict()
# create an instance of AccessPolicySpec from a dict
access_policy_spec_from_dict = AccessPolicySpec.from_dict(access_policy_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


