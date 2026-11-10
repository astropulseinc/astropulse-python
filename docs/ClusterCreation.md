# ClusterCreation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Identifies the cluster&#39;s create operation. | [optional] 
**cluster_name** | **str** | The cluster being created. | [optional] 
**message** | **str** | Says what happens next, in plain language. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Warnings about the cluster being created; the create goes ahead. | [optional] 
**status** | [**ClusterStatus**](ClusterStatus.md) | InProgress when creation started, or ApprovalPending when an organization owner must approve it first. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_creation import ClusterCreation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreation from a JSON string
cluster_creation_instance = ClusterCreation.from_json(json)
# print the JSON string representation of the object
print(ClusterCreation.to_json())

# convert the object into a dict
cluster_creation_dict = cluster_creation_instance.to_dict()
# create an instance of ClusterCreation from a dict
cluster_creation_from_dict = ClusterCreation.from_dict(cluster_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


