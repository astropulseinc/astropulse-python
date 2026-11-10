# ServiceAccountKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The key&#39;s lifetime as a number and unit (h, m or s), such as 720h for 30 days. Defaults to 24h. | [optional] 
**is_permanent** | **bool** | Creates a credential without an expiry when true. | [optional] 
**name** | **str** | Labels this credential, up to 100 characters. | [optional] 

## Example

```python
from astropulse._generated.models.service_account_key_request import ServiceAccountKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountKeyRequest from a JSON string
service_account_key_request_instance = ServiceAccountKeyRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountKeyRequest.to_json())

# convert the object into a dict
service_account_key_request_dict = service_account_key_request_instance.to_dict()
# create an instance of ServiceAccountKeyRequest from a dict
service_account_key_request_from_dict = ServiceAccountKeyRequest.from_dict(service_account_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


