# AccessPolicyKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** | When the key stops working; omit it for a key that does not expire. | [optional] 
**label** | **str** | Names who the key is for, at most 63 characters. | 

## Example

```python
from astropulse._generated.models.access_policy_key_request import AccessPolicyKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyKeyRequest from a JSON string
access_policy_key_request_instance = AccessPolicyKeyRequest.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyKeyRequest.to_json())

# convert the object into a dict
access_policy_key_request_dict = access_policy_key_request_instance.to_dict()
# create an instance of AccessPolicyKeyRequest from a dict
access_policy_key_request_from_dict = AccessPolicyKeyRequest.from_dict(access_policy_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


