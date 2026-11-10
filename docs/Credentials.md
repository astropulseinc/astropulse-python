# Credentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, str]** | Static credential values, e.g. AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY, or GOOGLE_APPLICATION_CREDENTIALS; omit it for &#x60;Dynamic&#x60; and &#x60;Vault&#x60;. Values are stored by AstroPulse and never returned; send new values to replace them, never a masked one. | [optional] 
**type** | [**CredentialType**](CredentialType.md) | Where the cluster&#39;s cloud credentials come from. Send keys in data only with &#x60;Static&#x60;. | 

## Example

```python
from astropulse._generated.models.credentials import Credentials

# TODO update the JSON string below
json = "{}"
# create an instance of Credentials from a JSON string
credentials_instance = Credentials.from_json(json)
# print the JSON string representation of the object
print(Credentials.to_json())

# convert the object into a dict
credentials_dict = credentials_instance.to_dict()
# create an instance of Credentials from a dict
credentials_from_dict = Credentials.from_dict(credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


