# AccessPolicyKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | When the key was created. | [optional] 
**expires_at** | **str** | When the key stops working; absent for a key that does not expire. | [optional] 
**id** | **str** | Identifies the key; revoke it by this ID. | [optional] 
**label** | **str** | Names who the key is for. | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_key import AccessPolicyKey

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyKey from a JSON string
access_policy_key_instance = AccessPolicyKey.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyKey.to_json())

# convert the object into a dict
access_policy_key_dict = access_policy_key_instance.to_dict()
# create an instance of AccessPolicyKey from a dict
access_policy_key_from_dict = AccessPolicyKey.from_dict(access_policy_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


