# ApplicationRollbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** | An optional idempotency key. If omitted the server generates one. | [optional] 
**reason** | **str** | An optional free-form audit reason. | [optional] 
**to_version** | **str** | The target Astro version (e.g. \&quot;v7\&quot;). Empty means the previous successful version. | [optional] 

## Example

```python
from astropulse._generated.models.application_rollback_request import ApplicationRollbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRollbackRequest from a JSON string
application_rollback_request_instance = ApplicationRollbackRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationRollbackRequest.to_json())

# convert the object into a dict
application_rollback_request_dict = application_rollback_request_instance.to_dict()
# create an instance of ApplicationRollbackRequest from a dict
application_rollback_request_from_dict = ApplicationRollbackRequest.from_dict(application_rollback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


