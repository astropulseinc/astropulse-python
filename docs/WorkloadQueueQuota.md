# WorkloadQueueQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | A Kubernetes quantity such as \&quot;64\&quot;. Empty means bounded only by the cluster itself. | [optional] 
**gpu** | **int** | How many accelerators the queue may hold across the cluster&#39;s GPU flavor. Checked against what the cluster&#39;s accelerator node groups and GPU node pools can ever provision. Unset and 0 differ: unset on the only queue means the whole ceiling, 0 means none. | [optional] 
**memory** | **str** | A Kubernetes quantity such as 256Gi. Empty means bounded only by the cluster itself. | [optional] 

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


