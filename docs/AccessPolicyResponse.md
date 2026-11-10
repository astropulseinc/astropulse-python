# AccessPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccessPolicy**](AccessPolicy.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_response import AccessPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyResponse from a JSON string
access_policy_response_instance = AccessPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyResponse.to_json())

# convert the object into a dict
access_policy_response_dict = access_policy_response_instance.to_dict()
# create an instance of AccessPolicyResponse from a dict
access_policy_response_from_dict = AccessPolicyResponse.from_dict(access_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


