# ClusterApprovalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterApproval**](ClusterApproval.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_approval_response import ClusterApprovalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterApprovalResponse from a JSON string
cluster_approval_response_instance = ClusterApprovalResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterApprovalResponse.to_json())

# convert the object into a dict
cluster_approval_response_dict = cluster_approval_response_instance.to_dict()
# create an instance of ClusterApprovalResponse from a dict
cluster_approval_response_from_dict = ClusterApprovalResponse.from_dict(cluster_approval_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


