# ClusterExposure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_manager** | [**ClusterExposureBrick**](ClusterExposureBrick.md) | The cert-manager and external-dns entries say who runs each brick. | [optional] 
**cluster_issuer** | [**ClusterExposureIssuer**](ClusterExposureIssuer.md) | The cert-manager ClusterIssuer exposed applications&#39; certificates come from, and what the agent observed of it. | [optional] 
**external_dns** | [**ClusterExposureBrick**](ClusterExposureBrick.md) |  | [optional] 
**gateway_path_reason** | **str** | Empty when an exposed application takes the gateway path on this cluster, otherwise why it keeps the Ingress path. | [optional] 
**load_balancer** | [**ClusterLoadBalancerExposure**](ClusterLoadBalancerExposure.md) | How endpoints on this cluster are made public or private. | [optional] 
**settings** | [**ClusterExposureSettings**](ClusterExposureSettings.md) | The cluster-level exposure settings a platform persona set (see ClusterExposureSettings). | [optional] 

## Example

```python
from astropulse._generated.models.cluster_exposure import ClusterExposure

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExposure from a JSON string
cluster_exposure_instance = ClusterExposure.from_json(json)
# print the JSON string representation of the object
print(ClusterExposure.to_json())

# convert the object into a dict
cluster_exposure_dict = cluster_exposure_instance.to_dict()
# create an instance of ClusterExposure from a dict
cluster_exposure_from_dict = ClusterExposure.from_dict(cluster_exposure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


