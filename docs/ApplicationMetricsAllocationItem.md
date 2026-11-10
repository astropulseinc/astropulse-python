# ApplicationMetricsAllocationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** | False when any contributing sample reported partial coverage. | [optional] 
**dimensions** | [**MetricsDimensions**](MetricsDimensions.md) | What was measured. | [optional] 
**name** | **str** | The application this reading belongs to. | [optional] 
**sample_count** | **int** | How many stored samples this window-averaged reading is built from. Complete is false if any one of them reported partial coverage — render as partial, never averaged in as if whole. | [optional] 

## Example

```python
from astropulse._generated.models.application_metrics_allocation_item import ApplicationMetricsAllocationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetricsAllocationItem from a JSON string
application_metrics_allocation_item_instance = ApplicationMetricsAllocationItem.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetricsAllocationItem.to_json())

# convert the object into a dict
application_metrics_allocation_item_dict = application_metrics_allocation_item_instance.to_dict()
# create an instance of ApplicationMetricsAllocationItem from a dict
application_metrics_allocation_item_from_dict = ApplicationMetricsAllocationItem.from_dict(application_metrics_allocation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


