# WorkloadQueueQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | The CPU the queue may use, such as 64. Left out, only the cluster limits it. | [optional] 
**gpu** | **int** | How many GPUs the queue may use, checked against what the cluster can provision; 0 means none. Left out, the only queue gets them all and a queue among several gets none. | [optional] 
**memory** | **str** | The memory the queue may use, such as 256Gi. Left out, only the cluster limits it. | [optional] 

## Example

```python
from astropulse._generated.models.workload_queue_quota import WorkloadQueueQuota

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadQueueQuota from a JSON string
workload_queue_quota_instance = WorkloadQueueQuota.from_json(json)
# print the JSON string representation of the object
print(WorkloadQueueQuota.to_json())

# convert the object into a dict
workload_queue_quota_dict = workload_queue_quota_instance.to_dict()
# create an instance of WorkloadQueueQuota from a dict
workload_queue_quota_from_dict = WorkloadQueueQuota.from_dict(workload_queue_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


