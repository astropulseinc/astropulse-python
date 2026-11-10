# CostPriceSheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_management_hour** | **str** | The hourly rate of the cluster&#39;s management fee, such as a managed control plane. Empty leaves a managed control plane&#39;s fee shown as not priced; zero means the cluster has no fee. | [optional] 
**cpu_core_hour** | **str** | The hourly rate for one CPU core. | [optional] 
**currency** | **str** | An ISO 4217 code; empty means USD. | [optional] [default to 'USD']
**gpu_hour** | **str** | The hourly rate for one GPU. | [optional] 
**gpu_node_label** | **str** | Identifies GPU capacity for clusters whose GPU nodes are not otherwise distinguishable. | [optional] 
**gpu_node_label_value** | **str** | The value GPUNodeLabel must carry to mark a node as GPU capacity. | [optional] 
**ram_gb_hour** | **str** | The hourly rate for one gigabyte of memory. | [optional] 
**spot_cpu_core_hour** | **str** | The hourly rate for one CPU core on a spot node. Applies only to nodes carrying SpotNodeLabel. | [optional] 
**spot_gpu_hour** | **str** | The hourly rate for one GPU on a spot node. | [optional] 
**spot_node_label** | **str** | Identifies spot capacity, as key and value. Providers differ (&#x60;cloud.google.com/gke-provisioning&#x3D;spot&#x60;, &#x60;eks.amazonaws.com/capacityType&#x3D;SPOT&#x60;, &#x60;kubernetes.azure.com/scalesetpriority&#x3D;spot&#x60;) and a self-managed pool may set its own, so the label is declared rather than assumed. Spot rates without a label are rejected: applied to every node they would under-report the whole cluster. | [optional] 
**spot_node_label_value** | **str** | The value SpotNodeLabel must carry to mark a node as spot capacity. | [optional] 
**spot_ram_gb_hour** | **str** | The hourly rate for one gigabyte of memory on a spot node. Required alongside SpotCPUCoreHour. | [optional] 
**storage_gb_hour** | **str** | The hourly rate for one gigabyte of storage. | [optional] 

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


