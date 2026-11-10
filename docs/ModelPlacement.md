# ModelPlacement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | **str** | The GPU model each replica asks for; empty when it names none. | [optional] 
**capacity_types** | **List[str]** | The purchase options the pool launches, in the order it prefers them: reserved, spot, on-demand. | [optional] 
**gpu_limit** | **int** | The most GPUs the pool may run at once across its nodes. | [optional] 
**gpus_at_max_replicas** | **int** | How many GPUs the model&#39;s maximum replica count would take of that limit. | [optional] 
**gpus_at_min_replicas** | **int** | How many GPUs the model&#39;s minimum replica count takes of that limit. | [optional] 
**gpus_per_replica** | **int** | How many GPUs one replica takes. | [optional] 
**instance_types** | [**List[ModelPlacementInstance]**](ModelPlacementInstance.md) | The instance types that can hold one replica, the one most likely to launch listed first. | [optional] 
**node_pool** | **str** | The GPU node pool that launches the replicas&#39; nodes. | [optional] 
**notes** | **List[str]** | Say the placement in sentences, for display. | [optional] 
**quota** | [**ModelPlacementQuota**](ModelPlacementQuota.md) | The cloud account quota one replica&#39;s node draws on. | [optional] 

## Example

```python
from astropulse._generated.models.model_placement import ModelPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPlacement from a JSON string
model_placement_instance = ModelPlacement.from_json(json)
# print the JSON string representation of the object
print(ModelPlacement.to_json())

# convert the object into a dict
model_placement_dict = model_placement_instance.to_dict()
# create an instance of ModelPlacement from a dict
model_placement_from_dict = ModelPlacement.from_dict(model_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


