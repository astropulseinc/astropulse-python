# ClusterDeletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**already_running** | **bool** | True when the cluster was already being deleted, so nothing new was started. | [optional] 
**cluster_id** | **str** | The id of the cluster&#39;s delete operation; empty on a dry run. | [optional] 
**dry_run** | [**ClusterDeleteDryRun**](ClusterDeleteDryRun.md) | Present only on a dry run, and says what the delete would leave in your cloud account. Nothing was deleted. | [optional] 
**message** | **str** | Says what happened; with recordOnly, it lists what is left in your cloud account. | [optional] 
**status** | [**ClusterStatus**](ClusterStatus.md) | The cluster&#39;s state once the delete was accepted; empty on a dry run. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_deletion import ClusterDeletion

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDeletion from a JSON string
cluster_deletion_instance = ClusterDeletion.from_json(json)
# print the JSON string representation of the object
print(ClusterDeletion.to_json())

# convert the object into a dict
cluster_deletion_dict = cluster_deletion_instance.to_dict()
# create an instance of ClusterDeletion from a dict
cluster_deletion_from_dict = ClusterDeletion.from_dict(cluster_deletion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


