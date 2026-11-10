# CloudAccountCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Says in one sentence what your team must do before AstroPulse can manage the cluster; empty when nothing. | [optional] 
**name** | **str** | The cluster&#39;s name. | [optional] 
**provisioner** | [**ProvisionerType**](ProvisionerType.md) | How the cluster is managed; omitted when AstroPulse does not know. | [optional] 
**state** | [**ClusterStatus**](ClusterStatus.md) | The cluster&#39;s state. | [optional] 
**state_tone** | [**StateTone**](StateTone.md) | How the state reads at a glance. | [optional] 

## Example

```python
from astropulse._generated.models.cloud_account_cluster import CloudAccountCluster

# TODO update the JSON string below
json = "{}"
# create an instance of CloudAccountCluster from a JSON string
cloud_account_cluster_instance = CloudAccountCluster.from_json(json)
# print the JSON string representation of the object
print(CloudAccountCluster.to_json())

# convert the object into a dict
cloud_account_cluster_dict = cloud_account_cluster_instance.to_dict()
# create an instance of CloudAccountCluster from a dict
cloud_account_cluster_from_dict = CloudAccountCluster.from_dict(cloud_account_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


