# ModelResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | [**ModelAccelerator**](ModelAccelerator.md) | The accelerator one replica needs, in AstroPulse&#39;s normalized vocabulary (the same identity the cluster&#39;s node groups declare with countPerNode). | [optional] 
**cpu** | **str** | The CPU budget for one replica, as a Kubernetes quantity (\&quot;2\&quot;, \&quot;500m\&quot;). Left unset, a generative model on GPUs gets 3 per GPU and any other model takes KServe&#39;s default. It matters most for CPU inference, where the runtime&#39;s throughput is the core count. | [optional] 
**memory** | **str** | The memory limit for one replica, as a Kubernetes quantity (\&quot;4Gi\&quot;). Defaults to 4Gi for a generative model on CPU and 8Gi on a GPU; raise it when a replica runs out of memory. | [optional] 

## Example

```python
from astropulse._generated.models.model_resources import ModelResources

# TODO update the JSON string below
json = "{}"
# create an instance of ModelResources from a JSON string
model_resources_instance = ModelResources.from_json(json)
# print the JSON string representation of the object
print(ModelResources.to_json())

# convert the object into a dict
model_resources_dict = model_resources_instance.to_dict()
# create an instance of ModelResources from a dict
model_resources_from_dict = ModelResources.from_dict(model_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


