# QueueMetricsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admission_count** | **float** | How many replicas were admitted across the range. | [optional] 
**admission_wait_mean_seconds** | **float** | The mean wait for quota. | [optional] 
**admission_wait_p50_seconds** | **float** | The median wait for quota across the range. | [optional] 
**admission_wait_p95_seconds** | **float** | The 95th-percentile wait for quota. | [optional] 
**cluster_queue** | **str** | The queue the replicas are admitted through. | [optional] 
**local_queue** | **str** | The application&#39;s own LocalQueue in its namespace. | [optional] 
**measured_seconds** | **float** | How much of the requested range had stored windows behind it. | [optional] 
**queue_admitted_workloads** | **float** | The ClusterQueue&#39;s admitted total across every tenant, averaged over the range. | [optional] 
**queue_pending_workloads** | **float** | The ClusterQueue&#39;s pending total across every tenant, averaged over the range. | [optional] 
**replicas_admitted** | **float** | The mean number of replicas holding admitted quota across the range. | [optional] 
**replicas_waiting** | **float** | The mean number of replicas waiting for quota. | [optional] 

## Example

```python
from astropulse._generated.models.queue_metrics_summary import QueueMetricsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of QueueMetricsSummary from a JSON string
queue_metrics_summary_instance = QueueMetricsSummary.from_json(json)
# print the JSON string representation of the object
print(QueueMetricsSummary.to_json())

# convert the object into a dict
queue_metrics_summary_dict = queue_metrics_summary_instance.to_dict()
# create an instance of QueueMetricsSummary from a dict
queue_metrics_summary_from_dict = QueueMetricsSummary.from_dict(queue_metrics_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


