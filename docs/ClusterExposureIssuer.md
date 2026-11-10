# ClusterExposureIssuer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**ClusterExposureCertificates**](ClusterExposureCertificates.md) | What endpoints get from this issuer. Empty when the cluster has no issuer. | [optional] 
**kind** | [**ClusterIssuerKind**](ClusterIssuerKind.md) | How the ClusterIssuer obtains certificates, as the cluster&#39;s agent observed it; absent when not observed. | [optional] 
**message** | **str** | The Ready condition&#39;s message, or why the issuer was not observed. | [optional] 
**name** | **str** | The ClusterIssuer&#39;s name; empty when the cluster has none. | [optional] 
**observed** | **bool** | Reports whether the cluster&#39;s agent reported this ClusterIssuer. | [optional] 
**ready** | **str** | The observed Ready condition: True, False or Unknown. Empty when not observed. | [optional] 
**refusal** | **str** | Empty when an application can be exposed with this issuer now; otherwise the reason a deploy is refused, as the deploy reports it. | [optional] 
**source** | [**ClusterExposureOwner**](ClusterExposureOwner.md) | Platform for the cert-manager add-on&#39;s own issuer, Cluster for one named by the cluster&#39;s exposure settings, None otherwise. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_exposure_issuer import ClusterExposureIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExposureIssuer from a JSON string
cluster_exposure_issuer_instance = ClusterExposureIssuer.from_json(json)
# print the JSON string representation of the object
print(ClusterExposureIssuer.to_json())

# convert the object into a dict
cluster_exposure_issuer_dict = cluster_exposure_issuer_instance.to_dict()
# create an instance of ClusterExposureIssuer from a dict
cluster_exposure_issuer_from_dict = ClusterExposureIssuer.from_dict(cluster_exposure_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


