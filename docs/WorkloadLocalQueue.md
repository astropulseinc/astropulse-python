# WorkloadLocalQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_queue** | **str** | The queue the namespace sends work to. Left out, it is &#x60;default&#x60;. | [optional] 
**name** | **str** | The connection&#39;s name. Left out, it is the queue&#39;s name. | [optional] 
**namespace** | **str** | The namespace that sends work to the queue; it must already exist. | [optional] 

## Example

```python
from astropulse._generated.models.workload_local_queue import WorkloadLocalQueue

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadLocalQueue from a JSON string
workload_local_queue_instance = WorkloadLocalQueue.from_json(json)
# print the JSON string representation of the object
print(WorkloadLocalQueue.to_json())

# convert the object into a dict
workload_local_queue_dict = workload_local_queue_instance.to_dict()
# create an instance of WorkloadLocalQueue from a dict
workload_local_queue_from_dict = WorkloadLocalQueue.from_dict(workload_local_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


