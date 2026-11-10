# AcceleratorMetricsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | **float** | The range-wide figures, each weighted by window length and each resting only on the windows that carried it. | [optional] 
**hardware_slowdown_fraction** | **float** | The mean fraction (0..1) of the range the hardware slowed a device, for a power brake or a fault. | [optional] 
**measured_seconds** | **float** | How much of the requested range had stored windows behind it. | [optional] 
**memory_total_bytes** | **float** |  | [optional] 
**memory_used_bytes** | **float** |  | [optional] 
**power_cap_fraction** | **float** | The mean fraction (0..1) of the range a device was slowed to stay under its power limit. | [optional] 
**power_watts** | **float** |  | [optional] 
**sm_occupancy** | **float** |  | [optional] 
**source** | **str** | The exporter they were read from, as on AcceleratorMetrics. | [optional] 
**temperature_celsius** | **float** |  | [optional] 
**thermal_fraction** | **float** | The mean fraction (0..1) of the range a device was slowed because it ran too hot. | [optional] 
**throttle_cause** | **str** | Says in a few words what slowed the devices: \&quot;Power limit\&quot;, which is normal under sustained full load, \&quot;Too hot\&quot; or \&quot;Hardware slowdown\&quot;. Empty when nothing did or the cause is unknown. | [optional] 
**throttled_fraction** | **float** |  | [optional] 
**utilization** | **float** |  | [optional] 
**vendor** | [**AcceleratorVendor**](AcceleratorVendor.md) | The maker of the accelerators these numbers came from; absent when the catalog does not define it. | [optional] 
**xid_errors** | **float** | The TOTAL across the range, not a mean: a fault is an event that happened, not a level that held. | [optional] 

## Example

```python
from astropulse._generated.models.accelerator_metrics_summary import AcceleratorMetricsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AcceleratorMetricsSummary from a JSON string
accelerator_metrics_summary_instance = AcceleratorMetricsSummary.from_json(json)
# print the JSON string representation of the object
print(AcceleratorMetricsSummary.to_json())

# convert the object into a dict
accelerator_metrics_summary_dict = accelerator_metrics_summary_instance.to_dict()
# create an instance of AcceleratorMetricsSummary from a dict
accelerator_metrics_summary_from_dict = AcceleratorMetricsSummary.from_dict(accelerator_metrics_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


