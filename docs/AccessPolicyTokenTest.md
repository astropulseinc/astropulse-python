# AccessPolicyTokenTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The JWT, with or without the Bearer prefix. | 

## Example

```python
from astropulse._generated.models.access_policy_token_test import AccessPolicyTokenTest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyTokenTest from a JSON string
access_policy_token_test_instance = AccessPolicyTokenTest.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyTokenTest.to_json())

# convert the object into a dict
access_policy_token_test_dict = access_policy_token_test_instance.to_dict()
# create an instance of AccessPolicyTokenTest from a dict
access_policy_token_test_from_dict = AccessPolicyTokenTest.from_dict(access_policy_token_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


