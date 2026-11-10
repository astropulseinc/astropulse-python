# WorkloadQueueingAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_queues** | [**List[WorkloadClusterQueue]**](WorkloadClusterQueue.md) | The queues a model application names in &#x60;model.queue.name&#x60;. Empty creates one queue named default whose GPU quota is the cluster&#39;s whole accelerator capacity. | [optional] 
**gang_scheduling** | [**WorkloadQueueingGangScheduling**](WorkloadQueueingGangScheduling.md) | Makes admission all-or-nothing: every pod of an admitted workload must be ready within the timeout, or the workload is evicted and requeued instead of holding partial capacity. | [optional] 
**integrations** | [**List[WorkloadQueueingIntegration]**](WorkloadQueueingIntegration.md) | The workload kinds the queues admit. Empty means batch/job only; any other kind needs that kind&#39;s operator installed. | [optional] 
**local_queues** | [**List[WorkloadLocalQueue]**](WorkloadLocalQueue.md) | Bind namespaces of yours to one of the ClusterQueues. An Application that names a queue gets its own LocalQueue without one here. | [optional] 

## Example

```python
from astropulse._generated.models.workload_queueing_addon_configuration import WorkloadQueueingAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadQueueingAddonConfiguration from a JSON string
workload_queueing_addon_configuration_instance = WorkloadQueueingAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(WorkloadQueueingAddonConfiguration.to_json())

# convert the object into a dict
workload_queueing_addon_configuration_dict = workload_queueing_addon_configuration_instance.to_dict()
# create an instance of WorkloadQueueingAddonConfiguration from a dict
workload_queueing_addon_configuration_from_dict = WorkloadQueueingAddonConfiguration.from_dict(workload_queueing_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


