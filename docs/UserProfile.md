# UserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The timestamp when the user account was created (RFC 3339 format) | [optional] 
**current_org_id** | **str** | The user&#39;s currently active organization ID | [optional] 
**email** | **str** | The user&#39;s email address | [optional] 
**identity_provider** | **str** | The sign-in method the user registered with. | [optional] 
**login_count** | **int** | The total number of times the user has logged in | [optional] 
**name** | **str** | The user&#39;s display name | [optional] 
**organization** | [**List[Organization]**](Organization.md) | Contains all organizations the user belongs to | [optional] 
**preferred_organization_id** | **str** | The user&#39;s default organization ID | [optional] 
**roles** | **List[str]** | The list of roles assigned to the user | [optional] 
**user_id** | **str** | The unique user identifier (UUID format) | [optional] 

## Example

```python
from astropulse._generated.models.user_profile import UserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfile from a JSON string
user_profile_instance = UserProfile.from_json(json)
# print the JSON string representation of the object
print(UserProfile.to_json())

# convert the object into a dict
user_profile_dict = user_profile_instance.to_dict()
# create an instance of UserProfile from a dict
user_profile_from_dict = UserProfile.from_dict(user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


