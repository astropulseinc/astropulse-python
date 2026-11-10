# WorkloadQueueingGangScheduling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Turns gang admission on. | [optional] 
**timeout** | **str** | How long every pod of an admitted workload has to become ready, as a duration such as 10m. Empty takes the AstroPulse default. | [optional] [default to '10m']

## Example

```python
from astropulse._generated.models.workload_queueing_gang_scheduling import WorkloadQueueingGangScheduling

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadQueueingGangScheduling from a JSON string
workload_queueing_gang_scheduling_instance = WorkloadQueueingGangScheduling.from_json(json)
# print the JSON string representation of the object
print(WorkloadQueueingGangScheduling.to_json())

# convert the object into a dict
workload_queueing_gang_scheduling_dict = workload_queueing_gang_scheduling_instance.to_dict()
# create an instance of WorkloadQueueingGangScheduling from a dict
workload_queueing_gang_scheduling_from_dict = WorkloadQueueingGangScheduling.from_dict(workload_queueing_gang_scheduling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


