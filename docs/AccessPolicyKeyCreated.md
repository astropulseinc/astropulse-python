# AccessPolicyKeyCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | When the key was created. | [optional] 
**expires_at** | **str** | When the key stops working; absent for a key that does not expire. | [optional] 
**id** | **str** | Identifies the key; revoke it by this ID. | [optional] 
**key** | **str** | The value callers send. Store it now: it cannot be read again. | [optional] 
**label** | **str** | Names who the key is for. | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_key_created import AccessPolicyKeyCreated

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyKeyCreated from a JSON string
access_policy_key_created_instance = AccessPolicyKeyCreated.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyKeyCreated.to_json())

# convert the object into a dict
access_policy_key_created_dict = access_policy_key_created_instance.to_dict()
# create an instance of AccessPolicyKeyCreated from a dict
access_policy_key_created_from_dict = AccessPolicyKeyCreated.from_dict(access_policy_key_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


