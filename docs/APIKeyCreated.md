# APIKeyCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The issuance timestamp. | [optional] 
**duration** | **str** | The configured lifetime; empty for permanent keys. | [optional] 
**expires_at** | **str** | The expiry timestamp; absent for permanent keys. | [optional] 
**id** | **str** | Identifies this credential. | [optional] 
**is_permanent** | **bool** | Indicates that this credential has no expiry. | [optional] 
**key** | **str** | The secret API key. Store it securely now: it cannot be retrieved again. | [optional] 
**last_used_at** | **str** | The most recently recorded successful authentication. | [optional] 
**masked_key** | **str** | A non-secret display representation of the credential. | [optional] 
**name** | **str** | Labels this credential. | [optional] 
**org_id** | **str** | Identifies the organization this credential may access. | [optional] 
**org_namespace** | **str** | The organization&#39;s short name. | [optional] 
**revoked_at** | **str** | The revocation timestamp, when revoked. | [optional] 
**revoked_by** | **str** | Identifies the administrator who revoked the credential. | [optional] 
**revoked_reason** | **str** | Explains why the credential was revoked. | [optional] 
**service_account_id** | **str** | The service account that owns the key; absent for personal keys. | [optional] 
**source** | [**APIKeySource**](APIKeySource.md) | Where the key was issued: CLI or UI for a personal key, API for a service account key. | [optional] 
**status** | [**APIKeyLifecycleStatus**](APIKeyLifecycleStatus.md) | The credential lifecycle state. | [optional] 
**user_id** | **str** | The user who owns a personal key; empty for service-account keys. | [optional] 

## Example

```python
from astropulse._generated.models.api_key_created import APIKeyCreated

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyCreated from a JSON string
api_key_created_instance = APIKeyCreated.from_json(json)
# print the JSON string representation of the object
print(APIKeyCreated.to_json())

# convert the object into a dict
api_key_created_dict = api_key_created_instance.to_dict()
# create an instance of APIKeyCreated from a dict
api_key_created_from_dict = APIKeyCreated.from_dict(api_key_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


