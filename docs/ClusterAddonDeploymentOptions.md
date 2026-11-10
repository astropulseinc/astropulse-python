# ClusterAddonDeploymentOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Validates the request and changes nothing. | [optional] 
**timeout** | **str** | Bounds that wait, as a duration (\&quot;10m\&quot;). | [optional] 
**wait_for_ready** | **bool** | The request open until the add-on is serving. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_deployment_options import ClusterAddonDeploymentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonDeploymentOptions from a JSON string
cluster_addon_deployment_options_instance = ClusterAddonDeploymentOptions.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonDeploymentOptions.to_json())

# convert the object into a dict
cluster_addon_deployment_options_dict = cluster_addon_deployment_options_instance.to_dict()
# create an instance of ClusterAddonDeploymentOptions from a dict
cluster_addon_deployment_options_from_dict = ClusterAddonDeploymentOptions.from_dict(cluster_addon_deployment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


