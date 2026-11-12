# CostVisibilityPrometheusStorageConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The cluster storage the disk uses, by the name bound on the cluster; it can&#39;t be changed after install. Left out, it is the cluster&#39;s default storage. | [optional] 
**size** | **str** | The disk size, from 1Gi to 2Ti. Left out, it is 20Gi. | [optional] [default to '20Gi']

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


