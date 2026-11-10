# CancelClusterOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Recorded with the cancellation. | [optional] 

## Example

```python
from astropulse._generated.models.cancel_cluster_operation_request import CancelClusterOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelClusterOperationRequest from a JSON string
cancel_cluster_operation_request_instance = CancelClusterOperationRequest.from_json(json)
# print the JSON string representation of the object
print(CancelClusterOperationRequest.to_json())

# convert the object into a dict
cancel_cluster_operation_request_dict = cancel_cluster_operation_request_instance.to_dict()
# create an instance of CancelClusterOperationRequest from a dict
cancel_cluster_operation_request_from_dict = CancelClusterOperationRequest.from_dict(cancel_cluster_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


