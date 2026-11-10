# WorkloadLocalQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_queue** | **str** | The LocalQueue binds to. Empty means default. | [optional] 
**name** | **str** | Of the LocalQueue. Empty takes the ClusterQueue&#39;s name. | [optional] 
**namespace** | **str** | The LocalQueue lives in. It must already exist. | [optional] 

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


