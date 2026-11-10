# AccessPolicyIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim** | **str** |  | [optional] 
**header** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_identity import AccessPolicyIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyIdentity from a JSON string
access_policy_identity_instance = AccessPolicyIdentity.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyIdentity.to_json())

# convert the object into a dict
access_policy_identity_dict = access_policy_identity_instance.to_dict()
# create an instance of AccessPolicyIdentity from a dict
access_policy_identity_from_dict = AccessPolicyIdentity.from_dict(access_policy_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


