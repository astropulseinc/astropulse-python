# ClusterExposureSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_issuer** | **str** | Names the cert-manager ClusterIssuer that signs exposed applications&#39; certificates when AstroPulse&#39;s cert-manager add-on is not installed on this cluster. Any issuer kind (ACME, CA, self-signed, Vault) is accepted once the cluster&#39;s agent reports it Ready. Empty clears the setting. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_exposure_settings import ClusterExposureSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExposureSettings from a JSON string
cluster_exposure_settings_instance = ClusterExposureSettings.from_json(json)
# print the JSON string representation of the object
print(ClusterExposureSettings.to_json())

# convert the object into a dict
cluster_exposure_settings_dict = cluster_exposure_settings_instance.to_dict()
# create an instance of ClusterExposureSettings from a dict
cluster_exposure_settings_from_dict = ClusterExposureSettings.from_dict(cluster_exposure_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


