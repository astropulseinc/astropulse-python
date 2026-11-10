# CostVisibilityPrometheusStorageConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The cluster storage this volume uses, by the name bound on the cluster. Empty uses the cluster&#39;s default storage; once installed, the storage is immutable. | [optional] 
**size** | **str** | A Kubernetes storage quantity from 1Gi through 2Ti. Empty selects the Astro default. | [optional] [default to '20Gi']

## Example

```python
from astropulse._generated.models.cost_visibility_prometheus_storage_configuration import CostVisibilityPrometheusStorageConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CostVisibilityPrometheusStorageConfiguration from a JSON string
cost_visibility_prometheus_storage_configuration_instance = CostVisibilityPrometheusStorageConfiguration.from_json(json)
# print the JSON string representation of the object
print(CostVisibilityPrometheusStorageConfiguration.to_json())

# convert the object into a dict
cost_visibility_prometheus_storage_configuration_dict = cost_visibility_prometheus_storage_configuration_instance.to_dict()
# create an instance of CostVisibilityPrometheusStorageConfiguration from a dict
cost_visibility_prometheus_storage_configuration_from_dict = CostVisibilityPrometheusStorageConfiguration.from_dict(cost_visibility_prometheus_storage_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


