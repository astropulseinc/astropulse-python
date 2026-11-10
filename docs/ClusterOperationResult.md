# ClusterOperationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The cluster the operation acted on. | [optional] 
**error** | [**Failure**](Failure.md) | Contains failure details when the operation failed. | [optional] 
**message** | **str** | Provides human-readable details. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Say what the request did and the one next step. | [optional] 
**outcome** | [**Outcome**](Outcome.md) | Whether the request goes ahead, when it answers with notices. | [optional] 
**status** | [**ClusterStatus**](ClusterStatus.md) | The cluster&#39;s status once the operation returned. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_operation_result import ClusterOperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperationResult from a JSON string
cluster_operation_result_instance = ClusterOperationResult.from_json(json)
# print the JSON string representation of the object
print(ClusterOperationResult.to_json())

# convert the object into a dict
cluster_operation_result_dict = cluster_operation_result_instance.to_dict()
# create an instance of ClusterOperationResult from a dict
cluster_operation_result_from_dict = ClusterOperationResult.from_dict(cluster_operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


