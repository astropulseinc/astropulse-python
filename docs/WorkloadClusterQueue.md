# WorkloadClusterQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohort** | **str** | A name shared by queues that lend each other unused quota: a queue in a cohort may borrow what the others are not using, and gives its own idle quota back in return. Queues sharing one pool of hardware usually share a cohort. Empty keeps this queue&#39;s quota strictly to itself. | [optional] 
**name** | **str** | What a model application sets in &#x60;model.queue.name&#x60; to run through this queue. | [optional] 
**preemption** | [**WorkloadQueuePreemption**](WorkloadQueuePreemption.md) | What happens when this queue is full and new work arrives. Omitted is LowerPriority. | [optional] 
**quota** | [**WorkloadQueueQuota**](WorkloadQueueQuota.md) | How much this queue may hold at once. The only queue takes the cluster&#39;s whole accelerator ceiling unless its quota sets gpu (an explicit 0 means no accelerators); a queue among several with gpu unset gets no GPU quota. | [optional] 

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


