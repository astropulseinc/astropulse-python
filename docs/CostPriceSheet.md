# CostPriceSheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_management_hour** | **str** | The hourly fee for managing the cluster, such as a managed control plane&#39;s. Left out, the fee shows as unpriced; 0 means there is none. | [optional] 
**cpu_core_hour** | **str** | The price of one CPU core for an hour. | [optional] 
**currency** | **str** | The currency of these prices, as a three-letter ISO 4217 code. Left out, it is USD. | [optional] [default to 'USD']
**gpu_hour** | **str** | The price of one GPU for an hour. | [optional] 
**gpu_node_label** | **str** | The node label that marks GPU nodes, for a cluster whose GPU nodes can&#39;t be told apart otherwise. | [optional] 
**gpu_node_label_value** | **str** | The value &#x60;gpuNodeLabel&#x60; must have for a node to count as a GPU node. | [optional] 
**ram_gb_hour** | **str** | The price of one gigabyte of memory for an hour. | [optional] 
**spot_cpu_core_hour** | **str** | The price of one CPU core for an hour on a Spot node, one carrying &#x60;spotNodeLabel&#x60;. | [optional] 
**spot_gpu_hour** | **str** | The price of one GPU for an hour on a Spot node. | [optional] 
**spot_node_label** | **str** | The node label that marks Spot nodes on your cloud, such as &#x60;eks.amazonaws.com/capacityType&#x3D;SPOT&#x60;. Required when Spot prices are set. | [optional] 
**spot_node_label_value** | **str** | The value &#x60;spotNodeLabel&#x60; must have for a node to count as Spot. | [optional] 
**spot_ram_gb_hour** | **str** | The price of one gigabyte of memory for an hour on a Spot node; set it with &#x60;spotCpuCoreHour&#x60;. | [optional] 
**storage_gb_hour** | **str** | The price of one gigabyte of storage for an hour. | [optional] 

## Example

```python
from astropulse._generated.models.cost_price_sheet import CostPriceSheet

# TODO update the JSON string below
json = "{}"
# create an instance of CostPriceSheet from a JSON string
cost_price_sheet_instance = CostPriceSheet.from_json(json)
# print the JSON string representation of the object
print(CostPriceSheet.to_json())

# convert the object into a dict
cost_price_sheet_dict = cost_price_sheet_instance.to_dict()
# create an instance of CostPriceSheet from a dict
cost_price_sheet_from_dict = CostPriceSheet.from_dict(cost_price_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


