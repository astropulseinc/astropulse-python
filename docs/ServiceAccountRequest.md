# ServiceAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Describes the automation, up to 1000 characters. | [optional] 
**name** | **str** | Labels the service account, up to 100 characters. It is unique among the organization&#39;s active service accounts; an archived account&#39;s name can be used again. | 
**role** | [**OrganizationRole**](OrganizationRole.md) | The account&#39;s organization role: Viewer, Editor or Admin. A service account is never an Owner. | 

## Example

```python
from astropulse._generated.models.service_account_request import ServiceAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountRequest from a JSON string
service_account_request_instance = ServiceAccountRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountRequest.to_json())

# convert the object into a dict
service_account_request_dict = service_account_request_instance.to_dict()
# create an instance of ServiceAccountRequest from a dict
service_account_request_from_dict = ServiceAccountRequest.from_dict(service_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


