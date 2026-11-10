# RollbackClusterAddonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Checks the rollback and reports what it would do, without changing the add-on. | [optional] 
**manual_approval** | **bool** | Confirms a rollback AstroPulse would otherwise hold. | [optional] 
**operation_id** | **str** | Ties this rollback to an operation already in flight. | [optional] 
**reason** | **str** | Recorded with the rollback. | [optional] 
**target_version** | **int** | The revision number to roll back to, from the add-on&#39;s history. A revision number, not a chart version. | 

## Example

```python
from astropulse._generated.models.rollback_cluster_addon_request import RollbackClusterAddonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackClusterAddonRequest from a JSON string
rollback_cluster_addon_request_instance = RollbackClusterAddonRequest.from_json(json)
# print the JSON string representation of the object
print(RollbackClusterAddonRequest.to_json())

# convert the object into a dict
rollback_cluster_addon_request_dict = rollback_cluster_addon_request_instance.to_dict()
# create an instance of RollbackClusterAddonRequest from a dict
rollback_cluster_addon_request_from_dict = RollbackClusterAddonRequest.from_dict(rollback_cluster_addon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


