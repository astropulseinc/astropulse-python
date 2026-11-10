# ClusterUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The unique cluster identifier | [optional] 
**message** | **str** | Provides human-readable details about the update result | [optional] 
**notices** | [**List[Notice]**](Notice.md) | What the update does, what an update sent with replaceRunning does, and warnings about the cluster it leaves; a warning doesn&#39;t stop the update. | [optional] 
**result** | [**ClusterUpdateResult**](ClusterUpdateResult.md) | What the update did. &#x60;Started&#x60; answers 202; &#x60;Unchanged&#x60; and &#x60;CredentialsStored&#x60; answer 200. | [optional] 
**status** | [**ClusterStatus**](ClusterStatus.md) | The current cluster status after the update operation | [optional] 

## Example

```python
from astropulse._generated.models.cluster_update import ClusterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterUpdate from a JSON string
cluster_update_instance = ClusterUpdate.from_json(json)
# print the JSON string representation of the object
print(ClusterUpdate.to_json())

# convert the object into a dict
cluster_update_dict = cluster_update_instance.to_dict()
# create an instance of ClusterUpdate from a dict
cluster_update_from_dict = ClusterUpdate.from_dict(cluster_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


