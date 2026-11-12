# WorkloadClusterQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohort** | **str** | A group name for queues that lend each other unused capacity. Left out, the queue keeps its capacity to itself. | [optional] 
**name** | **str** | The queue&#39;s name, which a model application sets in &#x60;model.queue.name&#x60;. | [optional] 
**preemption** | [**WorkloadQueuePreemption**](WorkloadQueuePreemption.md) | What happens when the queue is full and new work arrives. Left out, it is &#x60;LowerPriority&#x60;. | [optional] 
**quota** | [**WorkloadQueueQuota**](WorkloadQueueQuota.md) | How much CPU, memory and GPU the queue may use at once. | [optional] 

## Example

```python
from astropulse._generated.models.workload_cluster_queue import WorkloadClusterQueue

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadClusterQueue from a JSON string
workload_cluster_queue_instance = WorkloadClusterQueue.from_json(json)
# print the JSON string representation of the object
print(WorkloadClusterQueue.to_json())

# convert the object into a dict
workload_cluster_queue_dict = workload_cluster_queue_instance.to_dict()
# create an instance of WorkloadClusterQueue from a dict
workload_cluster_queue_from_dict = WorkloadClusterQueue.from_dict(workload_cluster_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


