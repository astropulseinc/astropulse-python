# APIKeyFeatureFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_read_cache_disabled** | **bool** | True when cloud account reads are never served from a saved result. | [optional] 
**deploy_preview_access** | **bool** | True when the organization can use deploy previews. | [optional] 
**nova_chat_enabled** | **bool** | True when Nova chat is open to every member of the organization. | [optional] 

## Example

```python
from astropulse._generated.models.api_key_feature_flags import APIKeyFeatureFlags

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyFeatureFlags from a JSON string
api_key_feature_flags_instance = APIKeyFeatureFlags.from_json(json)
# print the JSON string representation of the object
print(APIKeyFeatureFlags.to_json())

# convert the object into a dict
api_key_feature_flags_dict = api_key_feature_flags_instance.to_dict()
# create an instance of APIKeyFeatureFlags from a dict
api_key_feature_flags_from_dict = APIKeyFeatureFlags.from_dict(api_key_feature_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


