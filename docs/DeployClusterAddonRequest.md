# DeployClusterAddonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ClusterAddonConfiguration**](ClusterAddonConfiguration.md) | The add-on&#39;s settings: at most one add-on block, the one belonging to the add-on being installed, beside availability and resources. | [optional] 
**options** | [**ClusterAddonDeploymentOptions**](ClusterAddonDeploymentOptions.md) | Control how the install is carried out. | [optional] 
**version** | **str** | The chart version to install. Omitted installs the default. | [optional] 

## Example

```python
from astropulse._generated.models.deploy_cluster_addon_request import DeployClusterAddonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeployClusterAddonRequest from a JSON string
deploy_cluster_addon_request_instance = DeployClusterAddonRequest.from_json(json)
# print the JSON string representation of the object
print(DeployClusterAddonRequest.to_json())

# convert the object into a dict
deploy_cluster_addon_request_dict = deploy_cluster_addon_request_instance.to_dict()
# create an instance of DeployClusterAddonRequest from a dict
deploy_cluster_addon_request_from_dict = DeployClusterAddonRequest.from_dict(deploy_cluster_addon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


