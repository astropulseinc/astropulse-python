# CostDimensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_core_hours** | **float** |  | [optional] 
**cpu_usage_core_hours** | **float** | Consumed CPU core-hours. CPUCoreHours above is the allocated (requested) amount, which is what spend is billed against; this is what the workload actually used. Comparing the two is what separates an idle over-provisioned workload from a right-sized one. Absent when the source cannot report usage. | [optional] 
**cpu_utilization_percent** | **float** | CPU used as a percentage of CPU allocated, already divided over matching windows. Use this rather than dividing CPUUsageCoreHours by CPUCoreHours: usage is optional per window, so those two totals can cover different window counts and their ratio is wrong. | [optional] 
**efficiency_percent** | **float** | The single headline for how much of what a workload reserved it actually used: CPU and memory usage over CPU and memory allocation, weighted by allocated hours. Storage and GPU are not included. It is a weighted mean of CPUUtilizationPercent and RAMUtilizationPercent below and therefore always lies between whichever of those are present, which is what lets it be rendered as their headline. When no window reported usage it falls back to the source&#39;s own efficiency figure. Absent when neither is available, and may exceed 100 when a workload consumes more than it reserved. | [optional] 
**gpu_hours** | **float** |  | [optional] 
**network_gb** | **float** | The data the workloads sent, in gigabytes, leaving out pods on the host network. It is measured and not priced: no cost includes network traffic. | [optional] 
**pv_gb_hours** | **float** |  | [optional] 
**ram_gb_hours** | **float** |  | [optional] 
**ram_usage_gb_hours** | **float** | Consumed memory GB-hours, paired with RAMGBHours the same way CPUUsageCoreHours is paired with CPUCoreHours. | [optional] 
**ram_utilization_percent** | **float** | The memory equivalent of CPUUtilizationPercent. | [optional] 

## Example

```python
from astropulse._generated.models.cost_dimensions import CostDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of CostDimensions from a JSON string
cost_dimensions_instance = CostDimensions.from_json(json)
# print the JSON string representation of the object
print(CostDimensions.to_json())

# convert the object into a dict
cost_dimensions_dict = cost_dimensions_instance.to_dict()
# create an instance of CostDimensions from a dict
cost_dimensions_from_dict = CostDimensions.from_dict(cost_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


