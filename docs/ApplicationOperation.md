# ApplicationOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | The user-facing application name. | [optional] 
**current_version** | **str** | The version deployed before the operation. | [optional] 
**message** | **str** | A human-readable status message. | [optional] 
**next_actions** | **List[str]** | Concrete follow-up commands for humans/automation. | [optional] 
**operation_id** | **str** | The idempotency/correlation id for this operation. | [optional] 
**phase** | [**ApplicationRollbackState**](ApplicationRollbackState.md) | The current Astro rollback/resume state. | [optional] 
**progress_url** | **str** | The polling/streaming endpoint for live progress. | [optional] 
**target_version** | **str** | The version being rolled back/resumed to. | [optional] 
**workflow_id** | **str** | AstroPulse&#39;s execution id for this operation. It is opaque: quote it in a support request, do not parse or store it. | [optional] 

## Example

```python
from astropulse._generated.models.application_operation import ApplicationOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationOperation from a JSON string
application_operation_instance = ApplicationOperation.from_json(json)
# print the JSON string representation of the object
print(ApplicationOperation.to_json())

# convert the object into a dict
application_operation_dict = application_operation_instance.to_dict()
# create an instance of ApplicationOperation from a dict
application_operation_from_dict = ApplicationOperation.from_dict(application_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


