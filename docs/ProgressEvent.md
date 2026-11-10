# ProgressEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster&#39;s identifier. | [optional] 
**cluster_name** | **str** | The cluster this happened on. | [optional] 
**labels** | **Dict[str, str]** | Carry extra context. | [optional] 
**level** | [**ProgressEventLevel**](ProgressEventLevel.md) | How severe the event is. | [optional] 
**message** | **str** | What happened. | [optional] 
**operation_id** | **str** | The operation this belongs to. | [optional] 
**operation_status** | [**OperationStatus**](OperationStatus.md) | How the operation ended, on the event that ended it. Omitted on every other event. | [optional] 
**operation_type** | [**OperationType**](OperationType.md) | What the operation does. | [optional] 
**phase** | [**ClusterOperationStep**](ClusterOperationStep.md) | The step of the operation the event happened in. Omitted when it belongs to no step, such as a preflight check. | [optional] 
**phase_label** | **str** | The step it happened in, in words, such as Creating node groups. Omitted when it belongs to no step. | [optional] 
**progress_percentage** | **int** | How far through the operation was, 0 to 100. | [optional] 
**raw_output** | **str** | The provisioner&#39;s own output, when there was any. | [optional] 
**timestamp** | **datetime** | When it happened. | [optional] 

## Example

```python
from astropulse._generated.models.progress_event import ProgressEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressEvent from a JSON string
progress_event_instance = ProgressEvent.from_json(json)
# print the JSON string representation of the object
print(ProgressEvent.to_json())

# convert the object into a dict
progress_event_dict = progress_event_instance.to_dict()
# create an instance of ProgressEvent from a dict
progress_event_from_dict = ProgressEvent.from_dict(progress_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


