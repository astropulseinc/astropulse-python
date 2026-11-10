# ModelServing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_format** | [**ModelAPIFormat**](ModelAPIFormat.md) | The API the endpoint speaks. Omitted, a generative runtime serves its OpenAI-compatible API and any other runtime its own prediction API. | [optional] 
**kv_cache_size** | **str** | The memory the generative runtime reserves for its KV cache, as a Kubernetes quantity (\&quot;2Gi\&quot;): out of resources.memory on CPU, device memory per GPU on a GPU. Defaults to a quarter of resources.memory on CPU and to what the runtime works out from the device on a GPU; an embedding model ignores it. | [optional] 
**max_concurrent_requests** | **int** | The most requests one replica serves at once; further requests wait, where scaling.metric.requestsWaiting counts them. Defaults to two per CPU core on CPU and to the runtime&#39;s own limit on a GPU. | [optional] 
**max_context_tokens** | **int** | Caps the context window the runtime allocates for. | [optional] 
**multimodal** | [**ModelMultimodal**](ModelMultimodal.md) | Caps how many media items one request may carry, for a vision, video or audio model. Such a model is one model, not a pipeline: the generative runtime loads the encoder in the same process and accepts image, video and audio parts on the same chat-completions endpoint the text-only model answers on.  These are per-request limits the runtime allocates for, not quotas applied after the fact. The engine reserves memory against them when it starts, so raising a limit costs memory on every replica whether or not a caller ever sends that many items, and a request carrying more than the limit is refused rather than queued. Leaving a modality unset keeps the runtime&#39;s own limit for it.  Generative runtimes only, and refused behind a serving runtime AstroPulse did not install: the limit resolves into that runtime&#39;s own flag, and AstroPulse renders flags only for the runtimes it installs. | [optional] 

## Example

```python
from astropulse._generated.models.model_serving import ModelServing

# TODO update the JSON string below
json = "{}"
# create an instance of ModelServing from a JSON string
model_serving_instance = ModelServing.from_json(json)
# print the JSON string representation of the object
print(ModelServing.to_json())

# convert the object into a dict
model_serving_dict = model_serving_instance.to_dict()
# create an instance of ModelServing from a dict
model_serving_from_dict = ModelServing.from_dict(model_serving_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


