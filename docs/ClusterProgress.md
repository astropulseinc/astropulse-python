# ClusterProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster&#39;s identifier. | [optional] 
**cluster_name** | **str** | The cluster this operation runs against. | [optional] 
**completed_at** | **datetime** | When it finished, absent while it runs. | [optional] 
**current_phase** | [**ClusterOperationStep**](ClusterOperationStep.md) | The step the operation is on. Omitted when it is on no step, such as while it runs its preflight checks or once it has ended. | [optional] 
**last_update** | **datetime** | When this record last changed. | [optional] 
**message** | **str** | The latest human-readable line. | [optional] 
**metadata** | **Dict[str, str]** | Carries operation-specific values. | [optional] 
**operation_id** | **str** | Identifies this operation; pass it to the progress endpoints to follow it. | [optional] 
**operation_type** | [**OperationType**](OperationType.md) | What the operation does. | [optional] 
**organization_id** | **str** | Owns the cluster. | [optional] 
**progress_percentage** | **int** | How far through it is, 0 to 100. | [optional] 
**recent_events** | [**List[ProgressEvent]**](ProgressEvent.md) | The tail of the event stream, newest last. | [optional] 
**started_at** | **datetime** | When the operation began. | [optional] 
**status** | [**OperationStatus**](OperationStatus.md) | Where it has got to. | [optional] 
**superseded_by** | **str** | Set in the operation history on a failed create, delete or add-on apply once a later one of the same kind has completed, and holds that operation&#39;s ID. | [optional] 
**user_id** | **str** | Who asked for the operation. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_progress import ClusterProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProgress from a JSON string
cluster_progress_instance = ClusterProgress.from_json(json)
# print the JSON string representation of the object
print(ClusterProgress.to_json())

# convert the object into a dict
cluster_progress_dict = cluster_progress_instance.to_dict()
# create an instance of ClusterProgress from a dict
cluster_progress_from_dict = ClusterProgress.from_dict(cluster_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


