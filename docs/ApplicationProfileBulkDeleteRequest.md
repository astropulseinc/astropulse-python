# ApplicationProfileBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_names** | **List[str]** |  | 

## Example

```python
from astropulse._generated.models.application_profile_bulk_delete_request import ApplicationProfileBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProfileBulkDeleteRequest from a JSON string
application_profile_bulk_delete_request_instance = ApplicationProfileBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationProfileBulkDeleteRequest.to_json())

# convert the object into a dict
application_profile_bulk_delete_request_dict = application_profile_bulk_delete_request_instance.to_dict()
# create an instance of ApplicationProfileBulkDeleteRequest from a dict
application_profile_bulk_delete_request_from_dict = ApplicationProfileBulkDeleteRequest.from_dict(application_profile_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


