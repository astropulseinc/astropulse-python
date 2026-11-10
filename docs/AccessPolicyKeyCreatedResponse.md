# AccessPolicyKeyCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccessPolicyKeyCreated**](AccessPolicyKeyCreated.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_key_created_response import AccessPolicyKeyCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyKeyCreatedResponse from a JSON string
access_policy_key_created_response_instance = AccessPolicyKeyCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyKeyCreatedResponse.to_json())

# convert the object into a dict
access_policy_key_created_response_dict = access_policy_key_created_response_instance.to_dict()
# create an instance of AccessPolicyKeyCreatedResponse from a dict
access_policy_key_created_response_from_dict = AccessPolicyKeyCreatedResponse.from_dict(access_policy_key_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


