# ClusterInfrastructureEstimate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges** | [**List[ClusterInfrastructureCharge]**](ClusterInfrastructureCharge.md) | The charges outside the cluster&#39;s nodes, which are priced on their machine types. | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud. | [optional] 
**provisioner** | [**ProvisionerType**](ProvisionerType.md) | The provisioner the cluster is created with. | [optional] 
**region** | **str** | The cloud region. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_infrastructure_estimate import ClusterInfrastructureEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInfrastructureEstimate from a JSON string
cluster_infrastructure_estimate_instance = ClusterInfrastructureEstimate.from_json(json)
# print the JSON string representation of the object
print(ClusterInfrastructureEstimate.to_json())

# convert the object into a dict
cluster_infrastructure_estimate_dict = cluster_infrastructure_estimate_instance.to_dict()
# create an instance of ClusterInfrastructureEstimate from a dict
cluster_infrastructure_estimate_from_dict = ClusterInfrastructureEstimate.from_dict(cluster_infrastructure_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


