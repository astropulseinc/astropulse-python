# WorkloadQueueingAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_queues** | [**List[WorkloadClusterQueue]**](WorkloadClusterQueue.md) | The queues that share the cluster&#39;s capacity; a model application picks one in &#x60;model.queue.name&#x60;. Left out, one queue named &#x60;default&#x60; gets the cluster&#39;s whole GPU capacity. | [optional] 
**gang_scheduling** | [**WorkloadQueueingGangScheduling**](WorkloadQueueingGangScheduling.md) | Starts a workload only when all its pods can run: if they aren&#39;t all ready within the timeout, it is stopped and queued again. | [optional] 
**integrations** | [**List[WorkloadQueueingIntegration]**](WorkloadQueueingIntegration.md) | The kinds of workload the queues accept; a kind other than batch/job needs its own controller on the cluster. Left out, only batch/job is accepted. | [optional] 
**local_queues** | [**List[WorkloadLocalQueue]**](WorkloadLocalQueue.md) | Connects namespaces of yours to a queue. An application that names a queue gets its own connection without one here. | [optional] 

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


