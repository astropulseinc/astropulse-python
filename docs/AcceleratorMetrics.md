# AcceleratorMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | **float** | The mean number of devices attributed to the application&#39;s pods. Fractional means its replica count changed mid-window, not that a device was shared. | [optional] 
**hardware_slowdown_fraction** | **float** | The mean fraction (0..1) of the window the hardware slowed a device, for a power brake or a fault. | [optional] 
**memory_total_bytes** | **float** |  | [optional] 
**memory_used_bytes** | **float** | The framebuffer memory the application held and MemoryTotalBytes the devices&#39; capacity. Used alone is not comparable: 20GB means different things on an L4 and an H100. | [optional] 
**power_cap_fraction** | **float** | The mean fraction (0..1) of the window a device was slowed to stay under its power limit. | [optional] 
**power_watts** | **float** | The mean board power draw, summed across the devices. | [optional] 
**sm_occupancy** | **float** | The mean fraction (0..1) of resident warp slots in use. High utilization with low occupancy is a batch size too small to fill the accelerator. Absent on devices publishing no profiling counters. | [optional] 
**source** | **str** | The exporter they were read from, so a reader can tell why a field is absent rather than guessing. | [optional] 
**temperature_celsius** | **float** | The mean device temperature, averaged across them. | [optional] 
**thermal_fraction** | **float** | The mean fraction (0..1) of the window a device was slowed because it ran too hot. | [optional] 
**throttle_cause** | **str** | Says in a few words what slowed the devices: \&quot;Power limit\&quot;, which is normal under sustained full load, \&quot;Too hot\&quot; or \&quot;Hardware slowdown\&quot;. Empty when nothing did or the cause is unknown. | [optional] 
**throttled_fraction** | **float** | The mean fraction (0..1) of the window a device ran slower because of a power cap, a thermal limit or a hardware slowdown. | [optional] 
**utilization** | **float** | The mean fraction (0..1) of the window the devices were executing any kernel. It says a device was busy, not that it was working hard -- that is SMOccupancy. | [optional] 
**vendor** | [**AcceleratorVendor**](AcceleratorVendor.md) | The maker of the accelerators these numbers came from; absent when the catalog does not define it. | [optional] 
**xid_errors** | **float** | How many XID faults the devices reported during the window. Above zero is a hardware or driver fault -- the signal behind a model that dies with no OOM and nothing in its own logs. | [optional] 

## Example

```python
from astropulse._generated.models.accelerator_metrics import AcceleratorMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of AcceleratorMetrics from a JSON string
accelerator_metrics_instance = AcceleratorMetrics.from_json(json)
# print the JSON string representation of the object
print(AcceleratorMetrics.to_json())

# convert the object into a dict
accelerator_metrics_dict = accelerator_metrics_instance.to_dict()
# create an instance of AcceleratorMetrics from a dict
accelerator_metrics_from_dict = AcceleratorMetrics.from_dict(accelerator_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


