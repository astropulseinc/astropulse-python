# ClusterLoadBalancerExposure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_default** | [**EndpointExposureStatus**](EndpointExposureStatus.md) | The exposure a model endpoint on the gateway takes when it names none, the gateway add-on&#39;s; absent without the add-on. | [optional] 
**gateway_private** | **bool** | Reports whether the gateway add-on serves private model endpoints beside public ones. | [optional] 
**ingress_default** | [**EndpointExposureStatus**](EndpointExposureStatus.md) | The exposure of every Ingress endpoint, the nginx-ingress add-on&#39;s; absent without the add-on. | [optional] 
**load_balancer_default** | [**EndpointExposureStatus**](EndpointExposureStatus.md) | The exposure an application with accessType LoadBalancer takes when it names none: public. | [optional] 
**note** | **str** | A sentence about the cluster&#39;s load balancers, for example that every one is a Network Load Balancer on AWS. | [optional] 
**private_available** | **bool** | Reports whether this cluster can serve a private endpoint at all. | [optional] 
**private_refusal** | **str** | Why a private endpoint is refused on this cluster; empty when one can be served. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_load_balancer_exposure import ClusterLoadBalancerExposure

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLoadBalancerExposure from a JSON string
cluster_load_balancer_exposure_instance = ClusterLoadBalancerExposure.from_json(json)
# print the JSON string representation of the object
print(ClusterLoadBalancerExposure.to_json())

# convert the object into a dict
cluster_load_balancer_exposure_dict = cluster_load_balancer_exposure_instance.to_dict()
# create an instance of ClusterLoadBalancerExposure from a dict
cluster_load_balancer_exposure_from_dict = ClusterLoadBalancerExposure.from_dict(cluster_load_balancer_exposure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


