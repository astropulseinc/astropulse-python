# ModelServingCacheConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backing** | [**ModelCacheBacking**](ModelCacheBacking.md) | Where the weights are kept; required whenever &#x60;modelCache&#x60; is set. | [optional] 
**name** | **str** | The cluster storage binding that holds the weights. Required with Storage backing; it cannot be set with Node backing. | [optional] 
**node_groups** | **List[str]** | The node groups, CPU or GPU, and the GPU node pool, whose nodes hold the weights. A cached model runs on one of them. Leave out the groups that run the cluster&#39;s own components. | [optional] 
**size** | **str** | How much the cache may use, as a Kubernetes quantity such as 2Ti. Required with Storage backing; it cannot be set with Node backing, where the budget comes from the node&#39;s own disk. | [optional] 

## Example

```python
from astropulse._generated.models.model_serving_cache_configuration import ModelServingCacheConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ModelServingCacheConfiguration from a JSON string
model_serving_cache_configuration_instance = ModelServingCacheConfiguration.from_json(json)
# print the JSON string representation of the object
print(ModelServingCacheConfiguration.to_json())

# convert the object into a dict
model_serving_cache_configuration_dict = model_serving_cache_configuration_instance.to_dict()
# create an instance of ModelServingCacheConfiguration from a dict
model_serving_cache_configuration_from_dict = ModelServingCacheConfiguration.from_dict(model_serving_cache_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


