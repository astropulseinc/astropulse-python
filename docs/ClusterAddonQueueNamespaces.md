# ClusterAddonQueueNamespaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing** | **List[str]** | Namespaces of queued applications it gives no queue yet. | [optional] 
**unused** | **List[str]** | Namespaces it gives a queue where no queued application runs. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_queue_namespaces import ClusterAddonQueueNamespaces

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonQueueNamespaces from a JSON string
cluster_addon_queue_namespaces_instance = ClusterAddonQueueNamespaces.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonQueueNamespaces.to_json())

# convert the object into a dict
cluster_addon_queue_namespaces_dict = cluster_addon_queue_namespaces_instance.to_dict()
# create an instance of ClusterAddonQueueNamespaces from a dict
cluster_addon_queue_namespaces_from_dict = ClusterAddonQueueNamespaces.from_dict(cluster_addon_queue_namespaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


