# OrgFeatureFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_read_cache_disabled** | **bool** | Turns off keeping cloud-account read results for the org, so every read goes to the account. Off by default. | [optional] 
**deploy_preview_access** | **bool** |  | [optional] 
**nova_chat_enabled** | **bool** | The global rollout gate for Nova chat. When false (default), users must have a per-user grant (nova_users.nova_chat_access on the Nova orchestrator side) to use the chat. When true, chat is open to all org members. Flip globally to GA the feature. | [optional] 

## Example

```python
from astropulse._generated.models.org_feature_flags import OrgFeatureFlags

# TODO update the JSON string below
json = "{}"
# create an instance of OrgFeatureFlags from a JSON string
org_feature_flags_instance = OrgFeatureFlags.from_json(json)
# print the JSON string representation of the object
print(OrgFeatureFlags.to_json())

# convert the object into a dict
org_feature_flags_dict = org_feature_flags_instance.to_dict()
# create an instance of OrgFeatureFlags from a dict
org_feature_flags_from_dict = OrgFeatureFlags.from_dict(org_feature_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


