# ClusterCancellation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ended_at** | **datetime** | When the cancel finished. Omitted while Cancelling. | [optional] 
**operation** | [**ClusterOperationKind**](ClusterOperationKind.md) | The kind of operation that was cancelled: Update, Upgrade or Rollback. | [optional] 
**removed** | [**List[CancelCleanupItem]**](CancelCleanupItem.md) | Says, for each node group the operation was adding, whether it was removed. | [optional] 
**requested_at** | **datetime** | When the cancel reached the operation. | [optional] 
**status** | [**ClusterCancellationStatus**](ClusterCancellationStatus.md) | Where the cancel has got to: Cancelling while the operation stops and cleans up, then Cancelled. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_cancellation import ClusterCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCancellation from a JSON string
cluster_cancellation_instance = ClusterCancellation.from_json(json)
# print the JSON string representation of the object
print(ClusterCancellation.to_json())

# convert the object into a dict
cluster_cancellation_dict = cluster_cancellation_instance.to_dict()
# create an instance of ClusterCancellation from a dict
cluster_cancellation_from_dict = ClusterCancellation.from_dict(cluster_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


