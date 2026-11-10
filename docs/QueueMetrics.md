# QueueMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admission_count** | **float** | How many replicas were admitted during the window, the denominator behind the percentiles above. | [optional] 
**admission_wait_mean_seconds** | **float** | The mean wait for quota. | [optional] 
**admission_wait_p50_seconds** | **float** | The median wait for quota among replicas admitted during the window. | [optional] 
**admission_wait_p95_seconds** | **float** | The 95th-percentile wait for quota. | [optional] 
**cluster_queue** | **str** | The queue the replicas are admitted through. | [optional] 
**local_queue** | **str** | The application&#39;s own LocalQueue in its namespace. | [optional] 
**queue_admitted_workloads** | **float** | The ClusterQueue&#39;s admitted total across every tenant, averaged over the window: how busy the shared queue is. | [optional] 
**queue_pending_workloads** | **float** | The ClusterQueue&#39;s pending total across every tenant, averaged over the window. | [optional] 
**replicas_admitted** | **float** | The mean number of replicas holding admitted quota over the window. | [optional] 
**replicas_waiting** | **float** | The mean number of replicas waiting for quota. Above zero while the queue is at its quota means the queue is full, not the model slow. | [optional] 

## Example

```python
from astropulse._generated.models.queue_metrics import QueueMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of QueueMetrics from a JSON string
queue_metrics_instance = QueueMetrics.from_json(json)
# print the JSON string representation of the object
print(QueueMetrics.to_json())

# convert the object into a dict
queue_metrics_dict = queue_metrics_instance.to_dict()
# create an instance of QueueMetrics from a dict
queue_metrics_from_dict = QueueMetrics.from_dict(queue_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


