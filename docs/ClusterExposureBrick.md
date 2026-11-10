# ClusterExposureBrick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_routes** | **bool** | (external-dns only) reports whether HTTPRoute hostnames get a DNS record: the add-on applied with gatewayRoutes, or an observed controller running the gateway-httproute source. | [optional] 
**message** | **str** | One sentence about the brick. On externalDNS it says who writes the DNS record for an application&#39;s hostname: AstroPulse, a DNS controller you run, or you. | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** | The namespace and name locate the observed controller. | [optional] 
**observed** | **bool** | Reports whether the agent saw a running controller. | [optional] 
**owner** | [**ClusterExposureOwner**](ClusterExposureOwner.md) | Who runs the brick on the cluster. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_exposure_brick import ClusterExposureBrick

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExposureBrick from a JSON string
cluster_exposure_brick_instance = ClusterExposureBrick.from_json(json)
# print the JSON string representation of the object
print(ClusterExposureBrick.to_json())

# convert the object into a dict
cluster_exposure_brick_dict = cluster_exposure_brick_instance.to_dict()
# create an instance of ClusterExposureBrick from a dict
cluster_exposure_brick_from_dict = ClusterExposureBrick.from_dict(cluster_exposure_brick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


