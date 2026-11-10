# ModelQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Of the ClusterQueue, as declared under the workload-queueing add-on&#39;s configuration.workloadQueueing.clusterQueues on the target cluster (default when none is declared). | [optional] 

## Example

```python
from astropulse._generated.models.model_queue import ModelQueue

# TODO update the JSON string below
json = "{}"
# create an instance of ModelQueue from a JSON string
model_queue_instance = ModelQueue.from_json(json)
# print the JSON string representation of the object
print(ModelQueue.to_json())

# convert the object into a dict
model_queue_dict = model_queue_instance.to_dict()
# create an instance of ModelQueue from a dict
model_queue_from_dict = ModelQueue.from_dict(model_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


