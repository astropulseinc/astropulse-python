# AccessPolicyClaim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim** | **str** |  | [optional] 
**type** | [**AccessPolicyClaimType**](AccessPolicyClaimType.md) | How the claim is read. It defaults to List for scope and scp and to String otherwise. | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_claim import AccessPolicyClaim

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyClaim from a JSON string
access_policy_claim_instance = AccessPolicyClaim.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyClaim.to_json())

# convert the object into a dict
access_policy_claim_dict = access_policy_claim_instance.to_dict()
# create an instance of AccessPolicyClaim from a dict
access_policy_claim_from_dict = AccessPolicyClaim.from_dict(access_policy_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


