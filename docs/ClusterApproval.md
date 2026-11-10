# ClusterApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ClusterApprovalAction**](ClusterApprovalAction.md) | The decision that was sent. | [optional] 
**outcome** | [**ClusterApprovalOutcome**](ClusterApprovalOutcome.md) | What the decision did. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_approval import ClusterApproval

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterApproval from a JSON string
cluster_approval_instance = ClusterApproval.from_json(json)
# print the JSON string representation of the object
print(ClusterApproval.to_json())

# convert the object into a dict
cluster_approval_dict = cluster_approval_instance.to_dict()
# create an instance of ClusterApproval from a dict
cluster_approval_from_dict = ClusterApproval.from_dict(cluster_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


