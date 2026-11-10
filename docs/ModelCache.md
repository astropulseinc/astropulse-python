# ModelCache


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Turns the cache on for this application. | [optional] 
**node_group** | **str** | The node group, or GPU node pool, that holds the cached weights; every replica of the model then runs there. Needed only when more than one node group on the cluster could hold this model. | [optional] 
**size** | **str** | The artifact&#39;s size on disk, as a Kubernetes quantity (for example 30Gi), rounded up. Required when enabled. A model larger than the cache on the nodes it runs on is refused. | [optional] 

## Example

```python
from astropulse._generated.models.model_cache import ModelCache

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCache from a JSON string
model_cache_instance = ModelCache.from_json(json)
# print the JSON string representation of the object
print(ModelCache.to_json())

# convert the object into a dict
model_cache_dict = model_cache_instance.to_dict()
# create an instance of ModelCache from a dict
model_cache_from_dict = ModelCache.from_dict(model_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


