# ObservedNodeGPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_per_node** | **int** | How many of the devices each node has. | [optional] 
**model** | **str** | The device model, for example l4. Omitted when the nodes do not say. | [optional] 
**resource** | **str** | The resource name a workload requests the device by, for example nvidia.com/gpu. | [optional] 

## Example

```python
from astropulse._generated.models.observed_node_gpu import ObservedNodeGPU

# TODO update the JSON string below
json = "{}"
# create an instance of ObservedNodeGPU from a JSON string
observed_node_gpu_instance = ObservedNodeGPU.from_json(json)
# print the JSON string representation of the object
print(ObservedNodeGPU.to_json())

# convert the object into a dict
observed_node_gpu_dict = observed_node_gpu_instance.to_dict()
# create an instance of ObservedNodeGPU from a dict
observed_node_gpu_from_dict = ObservedNodeGPU.from_dict(observed_node_gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


