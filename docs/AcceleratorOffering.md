# AcceleratorOffering


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_seconds** | **int** | Seconds between scrapedAt and when this answer was made; absent when scrapedAt is. | [optional] 
**counts_per_node** | **List[int]** | Distinct device counts per machine across the carriers, ascending — exactly the valid countPerNode values for a node group&#39;s accelerator request. Empty when no carrier reports a whole-device count (fractional-GPU families). | [optional] 
**description** | **str** | What the device is for, in one sentence; absent for a model the catalog does not name. | [optional] 
**display_name** | **str** | The device&#39;s name as its maker writes it, such as NVIDIA L4; absent for a model the catalog does not name. | [optional] 
**kind** | [**AcceleratorKind**](AcceleratorKind.md) | The accelerator&#39;s class. | [optional] 
**machine_type_count** | **int** | Number of machine types in the region carrying this accelerator. | [optional] 
**machine_types** | **List[str]** | Machine types carrying this accelerator, the one behind the minimum on-demand price first, unpriced ones last. | [optional] 
**memory_mi_b** | **int** | Memory per accelerator device in MiB; absent when neither the provider nor the curated table reports it. | [optional] 
**min_on_demand_price_per_hour** | **str** | Lowest hourly on-demand price among the machine types carrying it; absent when none is priced. | [optional] 
**min_spot_price_per_hour** | **str** | Lowest hourly spot price among the machine types carrying it; absent when none is priced. | [optional] 
**model** | **str** | The normalised device name a node group&#39;s accelerator request names: \&quot;l4\&quot;, \&quot;a100\&quot;, \&quot;mi300x\&quot;. | [optional] 
**refresh_failed_at** | **str** | When the most recent refresh of this provider&#39;s catalog failed, RFC 3339; absent when the most recent refresh succeeded. The data shown is from scrapedAt. | [optional] 
**scraped_at** | **str** | When this offering&#39;s catalog data was last refreshed from the provider, RFC 3339. Provider pricing and availability may have changed since. | [optional] 
**stale** | **bool** | True when the data was last refreshed more than 48 hours ago, or never. Show its prices as out of date, not current. | [optional] 
**vendor** | [**AcceleratorVendor**](AcceleratorVendor.md) | The device&#39;s maker; absent when the provider names none the catalog defines. | [optional] 

## Example

```python
from astropulse._generated.models.accelerator_offering import AcceleratorOffering

# TODO update the JSON string below
json = "{}"
# create an instance of AcceleratorOffering from a JSON string
accelerator_offering_instance = AcceleratorOffering.from_json(json)
# print the JSON string representation of the object
print(AcceleratorOffering.to_json())

# convert the object into a dict
accelerator_offering_dict = accelerator_offering_instance.to_dict()
# create an instance of AcceleratorOffering from a dict
accelerator_offering_from_dict = AcceleratorOffering.from_dict(accelerator_offering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


