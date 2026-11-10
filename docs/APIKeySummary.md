# APIKeySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_key_count** | **int** | How many keys can authenticate now. | [optional] 
**expired_key_count** | **int** | How many keys are past their expiry. | [optional] 
**nearest_expiring_key** | [**APIKeyExpiration**](APIKeyExpiration.md) | The active key that expires first within the next 7 days; absent when none does. | [optional] 
**revoked_key_count** | **int** | How many keys were revoked. | [optional] 

## Example

```python
from astropulse._generated.models.api_key_summary import APIKeySummary

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeySummary from a JSON string
api_key_summary_instance = APIKeySummary.from_json(json)
# print the JSON string representation of the object
print(APIKeySummary.to_json())

# convert the object into a dict
api_key_summary_dict = api_key_summary_instance.to_dict()
# create an instance of APIKeySummary from a dict
api_key_summary_from_dict = APIKeySummary.from_dict(api_key_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


