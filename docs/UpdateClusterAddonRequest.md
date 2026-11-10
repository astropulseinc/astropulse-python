# UpdateClusterAddonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ClusterAddonConfiguration**](ClusterAddonConfiguration.md) | Replaces the add-on&#39;s settings; omitted keeps the stored ones, and with only availability or resources those change and the stored add-on block stays. At most one add-on block may be set, the one belonging to the add-on being updated. | [optional] 
**options** | [**ClusterAddonUpdateOptions**](ClusterAddonUpdateOptions.md) | Control how the update is carried out. | [optional] 
**target_version** | **str** | The add-on version to move to. Left out, the add-on keeps its current version and only its configuration changes. | [optional] 

## Example

```python
from astropulse._generated.models.update_cluster_addon_request import UpdateClusterAddonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterAddonRequest from a JSON string
update_cluster_addon_request_instance = UpdateClusterAddonRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterAddonRequest.to_json())

# convert the object into a dict
update_cluster_addon_request_dict = update_cluster_addon_request_instance.to_dict()
# create an instance of UpdateClusterAddonRequest from a dict
update_cluster_addon_request_from_dict = UpdateClusterAddonRequest.from_dict(update_cluster_addon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


