# ModelPlacementInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpus** | **int** | How many GPUs the instance carries. | [optional] 
**name** | **str** | The instance type, for example g6.xlarge. | [optional] 
**on_demand_price_per_hour** | **str** | The catalog&#39;s estimated on-demand price in USD per node-hour, when it has one. | [optional] 
**spot_price_per_hour** | **str** | The catalog&#39;s last observed spot price in USD per node-hour, when the pool may buy spot; spot prices change. | [optional] 
**vcpu** | **int** | How many vCPUs the instance carries. | [optional] 

## Example

```python
from astropulse._generated.models.model_placement_instance import ModelPlacementInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPlacementInstance from a JSON string
model_placement_instance_instance = ModelPlacementInstance.from_json(json)
# print the JSON string representation of the object
print(ModelPlacementInstance.to_json())

# convert the object into a dict
model_placement_instance_dict = model_placement_instance_instance.to_dict()
# create an instance of ModelPlacementInstance from a dict
model_placement_instance_from_dict = ModelPlacementInstance.from_dict(model_placement_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


