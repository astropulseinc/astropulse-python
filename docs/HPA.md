# HPA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_utilization_percentage** | **int** | The target CPU utilization percentage for scaling (required, range: 20-100) | 
**enabled** | **bool** | Enables or disables the horizontal pod autoscaler (required) | 
**max_replicas** | **int** | The maximum number of pod replicas (required, minimum: 1, must be &gt;&#x3D; MinReplicas) | 
**memory_utilization_percentage** | **int** | The target memory utilization percentage for scaling (required, range: 20-100) | 
**min_replicas** | **int** | The minimum number of pod replicas (required, minimum: 1) | 

## Example

```python
from astropulse._generated.models.hpa import HPA

# TODO update the JSON string below
json = "{}"
# create an instance of HPA from a JSON string
hpa_instance = HPA.from_json(json)
# print the JSON string representation of the object
print(HPA.to_json())

# convert the object into a dict
hpa_dict = hpa_instance.to_dict()
# create an instance of HPA from a dict
hpa_from_dict = HPA.from_dict(hpa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


