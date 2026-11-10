# ClusterAddonTLSExposure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **bool** | Reports whether one can be issued for a Gateway API route. | [optional] 
**ingress** | **bool** | Reports whether a certificate can be issued for an Ingress. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_tls_exposure import ClusterAddonTLSExposure

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonTLSExposure from a JSON string
cluster_addon_tls_exposure_instance = ClusterAddonTLSExposure.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonTLSExposure.to_json())

# convert the object into a dict
cluster_addon_tls_exposure_dict = cluster_addon_tls_exposure_instance.to_dict()
# create an instance of ClusterAddonTLSExposure from a dict
cluster_addon_tls_exposure_from_dict = ClusterAddonTLSExposure.from_dict(cluster_addon_tls_exposure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


