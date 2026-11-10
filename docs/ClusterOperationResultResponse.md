# ClusterOperationResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterOperationResult**](ClusterOperationResult.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_operation_result_response import ClusterOperationResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperationResultResponse from a JSON string
cluster_operation_result_response_instance = ClusterOperationResultResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterOperationResultResponse.to_json())

# convert the object into a dict
cluster_operation_result_response_dict = cluster_operation_result_response_instance.to_dict()
# create an instance of ClusterOperationResultResponse from a dict
cluster_operation_result_response_from_dict = ClusterOperationResultResponse.from_dict(cluster_operation_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


