# AccessPolicyJWT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **List[str]** | The aud values accepted; a token must carry at least one. | [optional] 
**identity** | [**AccessPolicyIdentity**](AccessPolicyIdentity.md) |  | [optional] 
**issuer** | **str** | The provider&#39;s issuer URL, exactly as its tokens carry it in iss. | [optional] 
**jwks_uri** | **str** | The provider&#39;s key set URL. Leave it empty to use the one the issuer&#39;s discovery document names. | [optional] 
**require** | [**List[AccessPolicyClaim]**](AccessPolicyClaim.md) | Lists claims a token must carry, each with the values accepted. | [optional] 

## Example

```python
from astropulse._generated.models.access_policy_jwt import AccessPolicyJWT

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyJWT from a JSON string
access_policy_jwt_instance = AccessPolicyJWT.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyJWT.to_json())

# convert the object into a dict
access_policy_jwt_dict = access_policy_jwt_instance.to_dict()
# create an instance of AccessPolicyJWT from a dict
access_policy_jwt_from_dict = AccessPolicyJWT.from_dict(access_policy_jwt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


