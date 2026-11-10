# ClusterAddonTLSReadiness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenges** | [**ClusterAddonTLSChallenges**](ClusterAddonTLSChallenges.md) | Lists the ACME challenge types the Let&#39;s Encrypt issuer can solve, and what each still needs when it cannot. | [optional] 
**cluster_issuer** | [**ClusterExposureIssuer**](ClusterExposureIssuer.md) | The ClusterIssuer exposure uses on this cluster and what the cluster&#39;s agent observed of it. Only on a read of an installed add-on; an apply response has no observation to report. | [optional] 
**exposure** | [**ClusterAddonTLSExposure**](ClusterAddonTLSExposure.md) | Says which exposure paths a certificate can be issued for. | [optional] 
**issuer** | [**ClusterAddonTLSIssuer**](ClusterAddonTLSIssuer.md) | The AstroPulse ClusterIssuer endpoint certificates come from. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Say what stops trusted certificates, or what is worth knowing about the certificates issued, each with the one step to take. | [optional] 
**trusted_certificates** | **bool** | Reports whether certificates browsers and clients trust can be issued on the cluster now. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_tls_readiness import ClusterAddonTLSReadiness

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonTLSReadiness from a JSON string
cluster_addon_tls_readiness_instance = ClusterAddonTLSReadiness.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonTLSReadiness.to_json())

# convert the object into a dict
cluster_addon_tls_readiness_dict = cluster_addon_tls_readiness_instance.to_dict()
# create an instance of ClusterAddonTLSReadiness from a dict
cluster_addon_tls_readiness_from_dict = ClusterAddonTLSReadiness.from_dict(cluster_addon_tls_readiness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


