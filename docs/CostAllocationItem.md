# CostAllocationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costs** | [**List[CostTotal]**](CostTotal.md) |  | [optional] 
**dimensions** | [**CostDimensions**](CostDimensions.md) |  | [optional] 
**group** | [**CostGroup**](CostGroup.md) | The group the row is shown under, from its kind. | [optional] 
**kind** | [**CostRowKind**](CostRowKind.md) | What the row is. | [optional] 
**name** | **str** | The namespace, application or node group the row is for. A row of a fixed kind is named by its code: its &#x60;kind&#x60;, such as &#x60;Idle&#x60;, or for a &#x60;ClusterInfrastructure&#x60; row its ClusterInfrastructureItem, such as &#x60;NATGateway&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.cost_allocation_item import CostAllocationItem

# TODO update the JSON string below
json = "{}"
# create an instance of CostAllocationItem from a JSON string
cost_allocation_item_instance = CostAllocationItem.from_json(json)
# print the JSON string representation of the object
print(CostAllocationItem.to_json())

# convert the object into a dict
cost_allocation_item_dict = cost_allocation_item_instance.to_dict()
# create an instance of CostAllocationItem from a dict
cost_allocation_item_from_dict = CostAllocationItem.from_dict(cost_allocation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


